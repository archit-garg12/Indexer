import lxml
from nltk.stem import PorterStemmer
from collections import defaultdict
from Posting import Posting

class Html_Reader:
    def __init__(self):
        self.ps = PorterStemmer()
    def read_file(self, root: 'etree', doc_id: int, inverted_index: {str:[Posting]}) -> None:
        position = 1
        position_words = defaultdict(list)
        for i in root.xpath('/html')[0].getiterator('*'):
            if i.tag not in {"script", "style"}:
                if i.text is not None:
                    temp = []
                    for c in i.text.strip("\n").lower():
                        char_number = ord(c)
                        if (48 <= char_number <= 57) or (97 <= char_number <= 122) or (48 <= char_number <= 57):
                            temp.append(c)
                        else:
                            temp.append(" ")
                    for words in "".join(temp).split(" "):
                        if words != "":
                            position_words[self.ps.stem(words)].append(position)
                            position += 1
        for key, val in position_words.items():
            post = Posting(doc_id)
            post.add_pos(val)
            post.add_tf(len(val)/(position-1))
            inverted_index[key].append(post)
            