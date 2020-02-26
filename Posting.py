class Posting():
    def __init__(self, doc_id:int):
        if type(doc_id) is int:
            self.doc_id = doc_id
            self.pos = []
            self.important = []
            self.tf = 0
        elif type(doc_id) is dict:
            self.doc_id = doc_id["doc_id"]
            self.tf = doc_id["tf"]

            if "pos" in doc_id:
                self.pos = doc_id["pos"]
            else:
                self.pos = []
            if "important" in doc_id:
                self.important = doc_id["important"]
            else:
                self.important = []
    def add_pos(self, positions: list) -> None:
        self.pos = positions
    def add_tf(self, term_freq:int) -> None:
        self.tf = term_freq
    def add_idf(self, term_idf: int) -> None:
        self.idf = term_idf
    def add_importance(self, i: int) -> None:
        self.important = i
    def get_pos(self) -> list:
        return self.pos
    def get_tf(self) -> int:
        return self.tf
    def get_idf(self) -> int:
        return self.idf
    def get_doc_id(self) -> int:
        return self.doc_id
    def get_importance(self) -> int:
        return self.important
    def __str__(self) -> str:
        if self.important == []:
            return str({"doc_id":self.doc_id, "pos":self.pos, "tf":self.tf})
        if self.pos == []:
            return str({"doc_id":self.doc_id, "important":self.important, "tf":self.tf})
        return str(self.__dict__)
        


    