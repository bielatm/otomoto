import requests
from bs4 import BeautifulSoup


class GetOtoMotoPage():

    def execute(self, url):
        response = requests.get(url)
        return response if response.ok else None


class ParsePage():

    def execute(self, html):
        parsed_html = BeautifulSoup(html)
        return parsed_html.body.find('div', attrs={'class': 'offers list'})
