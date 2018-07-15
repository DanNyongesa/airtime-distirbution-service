import collections
import json
import unittest
from queue import Queue
import os

from .. import Service, ServiceException

AT_USERNAME = 'sandbox'
AT_APIKEY = os.environ.get('AT_APIKEY') # provide your API KEy


class TestDisbursmentService(unittest.TestCase):
    def test_parse_csv(self):
        test_service = Service(username=AT_USERNAME, apikey=AT_APIKEY, csv_filename="not_found")

        self.assertRaises(ServiceException, test_service.parse_csv)
        test_service = Service(username=AT_USERNAME, apikey=AT_APIKEY, csv_filename="not_found.csv")

        self.assertRaises(ServiceException, test_service.parse_csv)

        test_service = Service(username=AT_USERNAME, apikey=AT_APIKEY, csv_filename="employee.csv")
        self.assertTrue(isinstance(test_service.parse_csv(), collections.Iterable))

    def test_send_airtime(self):
        test_service = Service(username=AT_USERNAME, apikey=AT_APIKEY, csv_filename="employee.csv")
        q = Queue()
        thread = test_service.send_airtime(_data=[{"phoneNumber": "+254703551421", "amount": "KES 5"},
                                                  {"phoneNumber": "+254712554404", "amount": "KES 23"}], _queue=q)
        while thread.is_alive():
            pass
        resp = q.get()
        q.task_done()
        # print(resp)
        resp = json.loads(resp.decode())

        self.assertTrue(resp["numSent"] == 2)


if __name__ == '__main__':
    unittest.main()
