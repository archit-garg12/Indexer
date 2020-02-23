class Url:
    def __init__(self, json_file):
        self._json_file = json_file

    def get_url(self):
        return self._json_file['url']

    def get_html(self):
        return self._json_file['content']