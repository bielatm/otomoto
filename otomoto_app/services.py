import requests


class GetOtoMotoPage():

    def execute(self, url):
        return requests.get(url).content
