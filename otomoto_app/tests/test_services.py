import responses
from unittest import TestCase
from otomoto_app.services import GetOtoMotoPage
from otomoto_app.constants import BASE_URL


class GetOtoMotoPageTest(TestCase):

    @responses.activate
    def test_request_response_ok(self):
        with open('otomoto_app/tests/html_otomoto.html', 'r') as file:
            content = file.read().replace('\n', '')

        responses.add(responses.GET, BASE_URL, body=content, status=200)
        service = GetOtoMotoPage()
        response = service.execute(url=BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, content)

    @responses.activate
    def test_request_response_not_ok(self):
        responses.add(responses.GET, BASE_URL, status=404)
        service = GetOtoMotoPage()
        response = service.execute(url=BASE_URL)
        self.assertIsNone(response)
