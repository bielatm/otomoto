import requests


class GetOtoMotoPage():

    def execute(self, url):
        response = requests.get(url)
        return response if response.ok else None
