from lxml import etree
from io import *
import json

class Url:
    def __init__(self, json_file: str):
        with open(json_file, encoding = 'utf-8') as json_file:
            data = json.load(json_file)
            self._url = data['url']
            self._content = data['content']

    def get_url(self) -> str:
        return self._url

    def get_html(self) -> 'Etree':
        html_value = self._content
        print(1)
        parser = etree.HTMLParser(encoding="utf-8")
        print(2)
        # print(StringIO(html_value))
        tree = etree.parse(StringIO(html_value), parser)
        print(3)
        print(type(tree.getroot()))
        return tree.getroot()

