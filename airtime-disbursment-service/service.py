# -*- encoding: utf-8 -*-

import csv
import json
import logging
import os
import pathlib
import re
import urllib.error
import urllib.parse
from urllib import request

BASE_DIR = os.path.abspath(os.getcwd())

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

sys_logger = logging.StreamHandler(sys.stdout)
sys_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sys_logger.setFormatter(formatter)
root.addHandler(sys_logger)

def phonenumber_isvalid(phonenumber: str) -> bool:
    """
    Given phonenumber it validates if its a valid phonenumber
    A valid phonenumber takes the format +(254) 7[0-9]
    :param phonenumber:
    :return: a correctly formated phone number in the format +2547XXXXXXXX

    >>> phonenumber_isvalid('+254703554404')
    True
    >>> phonenumber_isvalid('703554402')
    True
    >>> phonenumber_isvalid('70344h504')
    False
    >>> phonenumber_isvalid('254703554404')
    True
    """
    phonePattern = re.compile(r'''^
        (\d{3})     # area code is 3 digits (e.g. '254')
        \D*         # optional separator is any number of non-digits
        (7\d{2})     # trunk is 3 digits (e.g. '700') and starts with a 7
        \D*         # optional separator
        (\d{3})     # rest of number is 3 digits (e.g. '554')
        \D*         # optional separator
        (\d{3})       # remainder 3 digits
        $           # end of string
        ''', re.VERBOSE)
    phonenumber = phonenumber.strip('+')  # remove any preceding +
    phonenumber = phonenumber.strip('0')  # remove any preceedng 0
    if phonenumber.startswith('7'): phonenumber = '254{}'.format(phonenumber)  # ISO format
    return bool(phonePattern.search(phonenumber))


def amount_isvalid(amount: any) -> int:
    """
    Validates that the input given is a valid digit
    :raises ServiceException if the value is not a valid integer
    :param amount:
    :return:

    >>> amount_isvalid(20)
    True
    >>> amount_isvalid('20')
    True
    >>> amount_isvalid('2q1')
    False
    >>> amount_isvalid(20.1)
    True
    """
    try:
        return isinstance(float(amount), float)
    except ValueError as exc:
        logging.info("Invalid amount {}".format(amount))
        return False


class ServiceException(Exception):
    pass


class Service(object):
    def __init__(self, username=None, apikey=None, csv_filename=None):
        self._AT_PRODUCTION_DOMAIN = 'africastalking.com'
        self._AT_SANDBOX_DOMAIN = 'sandbox.africastalking.com'
        self._airtime_endpoint = '/version1/airtime/send'
        self._api_key = apikey
        self._username = username
        self._csv_filename = csv_filename
        self._request_headers = {}

        self.init_service(username, apikey, csv_filename)

    def init_service(self, username="sandbox", api_key="apikey", csv_filename='employee.csv'):
        """
        Initilize the service
        :param username: Africastalking username
        :param api_key: Africastalking apikey
        :return:
        """
        self._username = os.environ.get("AT_USERNAME", username)
        self._api_key = os.environ.get("AT_APIKEY", api_key)
        self._csv_filename = os.environ.get("CSV_FILENAME", csv_filename)
        self._request_headers = {
            'Accept': 'application/json',
            'User-Agent': 'africastalking-python/2.0.0',
            'ApiKey': self._api_key
        }
        if bool(self._username == 'sandbox'):
            self._base_url = 'https://api.' + self._AT_SANDBOX_DOMAIN
        else:
            self._base_url = 'https://api.' + self._AT_PRODUCTION_DOMAIN

    def _make_url(self, path):
        return self._base_url + path

    def _format_phonenumber(self, phonenumber: str) -> str:
        """
        Converts phonenumber to ISO format ie +2547XXXXXXXX
        :param phonenumber:
        :return:
        """
        if phonenumber.startswith('+'):
            return phonenumber
        if phonenumber.startswith('0'):
            return '+254{}'.format(phonenumber[1:])
        if phonenumber.startswith('2'):
            return '+{}'.format(phonenumber)

    def _format_amount(self, amount: float) -> str:
        """
        format amount into ISO format
        :param amount:
        :return:
        """
        return "KES {}".format(amount)

    def parse_csv(self) -> iter:
        """
        Parse the csv file
        For every row yield a tuple phone_number and amount
        :return:
        """
        file_path = os.path.join(BASE_DIR, 'assets/{}'.format(self._csv_filename))

        # verify the file is a csv file
        if pathlib.Path(file_path).suffix != '.csv':
            raise ServiceException("Please specify a .csv file")

        # raise an exception if the csv file isn't present
        if not os.path.exists(file_path):
            raise ServiceException("Can not find the specified csv file\nDid you put in in the assets folder?")

        # read csv file
        with open(file_path) as file:
            csv_reader = csv.reader(file)

            # validate amount and phone number
            recepients = filter(lambda row: phonenumber_isvalid(row[1]) and amount_isvalid(row[2]),
                                csv_reader)

            # merge duplicate fields
            _recepients = {}
            for name, phone_number, amount in recepients:
                if phone_number not in _recepients.keys():
                    _recepients[phone_number] = {"PhoneNumber": phone_number, "amount": amount}
                else:
                    amount = float(_recepients[phone_number]["amount"]) + float(amount)
                    _recepients[phone_number]["amount"] = amount

            # format the recepients list into the format [{"phoneNumber":"+254711XXXYYY","amount":"KES X"},{"phoneNumber":"+254733YYYZZZ","amount":"KES Y"}]
            recepients = map(
                lambda value: {"phoneNumber": self._format_phonenumber(value["PhoneNumber"]),
                               "amount": self._format_amount(value["amount"])},
                list(_recepients.values()))

            return recepients

    def send_airtime(self):
        """
        Send the specified amount of airtime to the specified phone_number
        :param phone_number:
        :param amount:
        :return:
        """
        data = {
            "username": self._username,
            "recipients": json.dumps(list(self.parse_csv()))
        }
        resp = self._make_request(data=data, method='POST',
                                  url=self._make_url(self._airtime_endpoint))
        decoded_resp = json.loads(resp)
        responses = decoded_resp["responses"]

        if self.responseCode == 201:
            if len(responses) > 0:
                logging.info("recived responses: {}".format(responses))
                return responses
            raise ServiceException(decoded_resp["errorMessage"])
        raise ServiceException(resp)

    def _make_request(self, data: dict, method: str, url: str):
        """
        Make a http call to Africastalking endpoint
        :param data: the payload
        :param method: HTTP verb {POST, GET, PUT} defaults to GET
        :param url: The url to make call to
        :return:
        """
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = request.Request(
            method=method,
            data=data,
            url=url,
            headers=self._request_headers
        )
        response = request.urlopen(req)
        self.responseCode = response.getcode()
        response = response.read()
        return response


if __name__ == "__main__":
    # test runner
    import doctest

    doctest.testmod()
