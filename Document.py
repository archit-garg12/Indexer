class Document_info:
    def __init__(self, query: str, doc_id: int):
        self._query = query
        self._doc_id = doc_id
        with open('indexes/index_master.txt', 'r') as f:
            self.

    def get_tfidf(self):
