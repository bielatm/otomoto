import unittest
import requests
from otomoto_app.services import GetOtoMotoPage


class GetOtoMotoPageTest(unittest.TestCase):

    def test_request_response(self):
        service = GetOtoMotoPage()
        response = service.execute(url='https://www.otomoto.pl/osobowe/')
        self.assertTrue(response.ok)
