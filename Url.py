from lxml import etree
from io import *
import json

class Url:
    def __init__(self, json_file: str):
        with open(json_file) as json_file:
            data = json.load(json_file)
            self._url = data['url']
            self._content = data['content']

    def get_url(self) -> str:
        return self._url

    def get_html(self) -> 'Etree ':
        html_value = self._content
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html_value), parser)
        return tree.getroot()

