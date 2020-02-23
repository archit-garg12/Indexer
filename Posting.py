class Posting():
    def __init__(self, doc_id:int):
        self.doc_id = doc_id
        self.pos = []
        self.tf = 0
        self.idf = 0
    def add_pos(self, positions: list) -> None:
        self.pos = positions
    def add_tf(self, term_freq:int) -> None:
        self.tf = term_freq
    def get_pos(self) -> list:
        return self.pos
    def get_tf(self) -> int:
        return self.tf
    def get_doc_id(self) -> int:
        return self.doc_id
    


    