# -*- encoding: utf-8 -*-

import csv
import os
import pathlib
import re

BASE_DIR = os.path.abspath(os.getcwd())


def validate_phonenumber(phonenumber: str) -> bool:
    """
    Given phonenumber it validates if its a valid phonenumber
    A valid phonenumber takes the format +(254) 7[0-9]
    :param phonenumber:
    :return: a correctly formated phone number in the format +2547XXXXXXXX

    >>> validate_phonenumber('+254703554404')
    True
    >>> validate_phonenumber('703554402')
    True
    >>> validate_phonenumber('70344h504')
    False
    >>> validate_phonenumber('254703554404')
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
    try:
        phonenumber = phonenumber.strip('+')  # remove any preceding +
        phonenumber = phonenumber.strip('0')  # remove any preceedng 0
        if phonenumber.startswith('7'): phonenumber = '254{}'.format(phonenumber)  # ISO format
        return bool(phonePattern.search(phonenumber))
    except ValueError:
        return False


def validate_amount(amount: any) -> int:
    """
    Validates that the input given is a valid digit
    :raises ServiceException if the value is not a valid integer
    :param amount:
    :return:

    >>> validate_amount(20)
    True
    >>> validate_amount('20')
    True
    >>> validate_amount('2q1')
    False
    >>> validate_amount(20.1)
    True
    """
    try:
        return isinstance(float(amount), float)
    except ValueError as exc:
        return False


class ServiceException(Exception):
    pass


class Service(object):
    def __init__(self):
        self.__base_url = 'http://api.africastalking.com/version1'
        self.__airtime_endpoint = '/airtime/send'
        self.__api_key = ''
        self.__username = ''
        self.__csv_filename = ''

    def init_service(self, username="sandbox", api_key="apikey", csv_filename='employee.csv'):
        """
        Initilize the service
        :param username: Africastalking username
        :param api_key: Africastalking apikey
        :return:
        """
        self.__username = os.environ.get("AT_USERNAME", username)
        self.__api_key = os.environ.get("AT_APIKEY", api_key)
        self.__csv_filename = os.environ.get("CASV_FILENAME", csv_filename)

    def __format_phonenumber(self, phonenumber: str) -> str:
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

    def __format_amount(self, amount: float) -> str:
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
        file_path = os.path.join(BASE_DIR, 'assets/{}'.format(self.__csv_filename))
        if pathlib.Path(file_path).suffix != '.csv':  # verify the file is a csv file
            raise ServiceException("Please specify a .csv file")
        if not os.path.exists(file_path):  # raise an exception if the csv file isn't present
            raise ServiceException("Can not find the specified csv file\nDid you put in in the assets folder?")
        with open(file_path) as file:  # read csv file
            return csv.reader(file)

    def send_airtime(self, phone_number: str, amount: int):
        """
        Send the specified amount of airtime to the specified phone_number
        :param phone_number:
        :param amount:
        :return:
        """
        # validate phone_number
        phone_number = validate_phonenumber(phone_number)
        amount = validate_amount(amount)
        req = self.__make_request(method='POST', url='', data={})
        pass

    def __make_request(self, data: dict, method: str, url: str):
        """
        Make a http call
        :param data: the payload
        :param method: HTTP verb {POST, GET, PUT} defaults to GET
        :param url: The url to make call to
        :return:
        """
        pass


if __name__ == "__main__":
    # test runner
    import doctest

    doctest.testmod()
