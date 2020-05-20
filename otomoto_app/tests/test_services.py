import requests
from unittest import TestCase
from unittest.mock import Mock, patch
from otomoto_app.services import GetOtoMotoPage


class GetOtoMotoPageTest(TestCase):

    @patch('otomoto_app.services.requests.get')
    def test_request_response(self, mock_get):
        mock_get.return_value.ok = True
        service = GetOtoMotoPage()
        response = service.execute(url='https://www.otomoto.pl/osobowe/')
        self.assertTrue(response)
