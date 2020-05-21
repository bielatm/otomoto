from unittest import TestCase
from unittest.mock import Mock, patch
from otomoto_app.services import GetOtoMotoPage
from otomoto_app.constants import BASE_URL


class GetOtoMotoPageTest(TestCase):

    @patch('otomoto_app.services.requests.get')
    def test_request_response_ok(self, mock_get):
        with open('otomoto_app/tests/html_otomoto.html', 'r') as file:
            content = file.read().replace('\n', '')

        mock_get.return_value = Mock(ok=True, content=content)
        service = GetOtoMotoPage()
        response = service.execute(url=BASE_URL)
        self.assertTrue(response)
        self.assertEqual(response.content, content)

    @patch('otomoto_app.services.requests.get')
    def test_request_response_not_ok(self, mock_get):
        mock_get.return_value = Mock(ok=False)
        service = GetOtoMotoPage()
        response = service.execute(url=BASE_URL)
        self.assertIsNone(response)
