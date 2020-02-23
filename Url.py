from lxml import etree
from io import *

class Url:
    def __init__(self, json_file: str):
        self._json_file = json_file

    def get_url(self) -> str:
        return self._json_file['url']

    def get_html(self) -> 'Etree ':
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html_value), parser)
        root = tree.getroot()
        return self._json_file['content']