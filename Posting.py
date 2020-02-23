class Posting():
    def __init__(self, doc_name:str, doc_id:int):
        self.doc_name = doc_name
        self.doc_id = doc_id
        self.token_attrib = {}
        self.tf_idf = 0

    