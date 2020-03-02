import lxml
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
from Posting import Posting
import math
from simhash import Simhash

class Html_Reader:
    def __init__(self):
        self.ps = SnowballStemmer("english")
        self.SIMHASH_URLS = {}
    def read_file(self, root: 'etree', doc_id: int, inverted_index: {str:[Posting]}) -> None:
        word = []
                        
        

        position = 1
        position_words = defaultdict(list)
        importance_word = defaultdict(list)
        for i in root.xpath('/html')[0].getiterator('*'):
            if i.tag not in {"script", "style"}:
                if i.text is not None:
                    word.append(i.text)
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
        # keeps a variable of a string of all the words to create a Simhash value
        val = ' '.join(word)
        temp_sim = Simhash(val)
        # checks if there are any duplicates or near duplicates in the Simhash set
        for i in self.SIMHASH_URLS:
            if i.distance(temp_sim) <= 1:
                print("simhashed", doc_id)
                return False
        self.SIMHASH_URLS[temp_sim] = doc_id
        for key, val in position_words.items():
            post = Posting(doc_id)
            post.add_pos(val)
            post.add_tf((len(val) + len(importance_word[key]))/(position-1))
            post.add_importance(importance_word[key])
            inverted_index[key].append(post)
        for key, val in importance_word.items():
            if key not in position_words:
                post = Posting(doc_id)
                post.add_tf((len(importance_word[key]))/(position-1))
                post.add_importance(importance_word[key])
                inverted_index[key].append(post)
        return True

    def porter_stem(self, word):
        return self.ps.stem(word)


    def read_master_for_id(self, master: str, write_file:str):
        print("inheere")
        print(master)
        wf = open(write_file, "w+")
        with open(master , "r+") as mas:
            for word in mas:
                wording = word.split("#")
                temp = eval(wording[1])
                final = []
                for x in temp:
                    p = Posting(eval(x))
                    p.add_idf(math.log(55393/len(temp)))
                    p.add_tfidf()
                    final.append(p)
                final = list(sorted(final , key= lambda x: -x.get_tfidf()))
                wf.write(wording[0]+ "#" + str([str(x) for x in final]) + "#\n")               
        wf.close()


  




