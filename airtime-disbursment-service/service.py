import os
import csv


class ServiceException(Exception):
    pass


class Service(object):
    def __init__(self):
        self.__base_url = 'http://api.africastalking.com/version1'
        self.__airtime_endpoint = '/airtime/send'
        self.__api_key = ''
        self.__username = ''

    def init_service(self, username="sandbox", api_key="apikey"):
        """
        Initilize the service
        :param username: Africastalking username
        :param api_key: Africastalking apikey
        :return:
        """
        self.__username = os.environ.get("AT_USERNAME", username)
        self.__api_key = os.environ.get("AT_APIKEY", api_key)

    def parse_csv(self) -> iter:
        """
        Parse the csv file
        For every row yield a tuple phone_number and amount
        :return:
        """
        pass

    def send_airtime(self, phone_number: str, amount: int):
        """
        Send the specified amount of airtime to the specified phone_number
        :param phone_number:
        :param amount:
        :return:
        """
        # validate phone_number
        phone_number = self.__validate_phonenumber(phone_number)
        amount = self.__validate_amount(amount)
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

    def __validate_phonenumber(self, phonenumber: str) -> str:
        """
        Given phonenumber it validates if its a valid phonenumber
        A valid phonenumber takes the format +(254) 7[0-9]
        :param phonenumber:
        :return: a correctly formated phone number in the format +2547XXXXXXXX
        """
        pass

    def __validate_amount(self, amount: any) -> int:
        """
        Validates that the input given is a valid digit
        :raises ServiceException if the value is not a valid integer
        :param amount:
        :return:
        """
        pass
