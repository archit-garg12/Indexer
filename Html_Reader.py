import lxml
from nltk.stem import PorterStemmer
from collections import defaultdict
from Posting import Posting
import math

class Html_Reader:
    def __init__(self):
        self.ps = PorterStemmer()
    def read_file(self, root: 'etree', doc_id: int, inverted_index: {str:[Posting]}) -> None:
        position = 1
        position_words = defaultdict(list)
        importance_word = defaultdict(list)
        for i in root.xpath('/html')[0].getiterator('*'):
            if i.tag not in {"script", "style"}:
                if i.text is not None:
                    temp = []
                    prevPos = position
                    for c in i.text.strip("\n").lower():
                        char_number = ord(c)
                        if (48 <= char_number <= 57) or (97 <= char_number <= 122):
                            temp.append(c)
                        else:
                            temp.append(" ")
                    for words in "".join(temp).split(" "):
                        if words != "":
                            
                            if i.tag in ["h1", "h2", "h3", "bold", "strong", "title"]:
                                importance_word[self.porter_stem(words)].append(position)
                            else:
                                position_words[self.porter_stem(words)].append(position)
                            position += 1
        for key, val in position_words.items():
            post = Posting(doc_id)
            post.add_pos(val)
            post.add_tf((len(val) + len(importance_word[key]))/(position-1))
            post.add_importance(importance_word[key])
            inverted_index[key].append(post)
        for key, val in position_words.items():
            if key not in position_words:
                post = Posting(doc_id)
                post.add_tf((len(importance_word[key]))/(position-1))
                post.add_importance(importance_word[key])
                inverted_index[key].append(post)

    def porter_stem(self, word):
        return self.ps.stem(word)


    # def read_master_for_id(self, master: str, write_file:str):
    #     print("inheere")
    #     print(master)
    #     wf = open(write_file, "a+")
    #     with open(master , "r+") as mas:
    #         for word in mas:
    #             wording = word.split("#")
    #             temp = eval(wording[1])
    #             final = []
    #             for x in temp:
    #                 p = Posting(eval(x))
    #                 p.add_idf(math.log(55393/len(temp)))
    #                 final.append(str(p))
    #             wf.write(wording[0]+ "#" + str(final) + "#\n")           
                    
    #     wf.close()


  




