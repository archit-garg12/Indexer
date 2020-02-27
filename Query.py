import os
from Posting import Posting
from collections import defaultdict
from Html_Reader import Html_Reader
class Query():
    def __init__(self, query, index):
        reader = Html_Reader()
        temp = []
        for c in query.strip("\n").lower():
            char_number = ord(c)
            if (48 <= char_number <= 57) or (97 <= char_number <= 122):
                temp.append(c)
            else:
                temp.append(" ")
        #prepped query to process using tokenization method
        self.query = [reader.porter_stem(x) for x in "".join(temp).split(" ")]
        #index is the ranges of letters to seek postions
        self.index = index
    def retrieve_query(self):
        useful_query = {}
        with open("indexes/index_master.txt", "r") as master:
            print(self.query)
            for words in self.query:
                #for each word limits range to first letter of word
                # curr = self.index[words[0]]
                # seek = curr
                # final = chr(ord(words[0]) + 1)
                # if words[0] == "9":
                #     final = "z"
                # if words[0] == "z":
                #     final = "end"
                # final = self.index[final]
                # mid = int((curr + final)/2)doc_list = []
                # master.seek(curr, 0)
                #read each line and check if the first
                words 
                if words in self.index:
                    
                    master.seek(self.index[words], 0)
                    useful_query[words] = eval(master.readline().split("#")[1])
                # while seek < final:
                    # s = master.readline()
                    # line = master.readline()
                    # mid = master.tell()
                  
                    # lines = line.strip("\n").split("#")
                    # seek += len(line)

                    # if lines[0] == words:
                    #     useful_query[words] = eval(lines[1])
                    #     break

        # print(useful_query)
        #sort dict by length of postings so process less posting lists first to easily determine overlap over multiple terms
        useful_query = sorted(useful_query.items(), key = lambda x: len(x[1]))
        document_ranks = defaultdict(int)
        accum = []
        for lists in useful_query:
            for l in lists[1]:
                p = Posting(eval(l))
                document_ranks[p.get_doc_id()] += 1
                if document_ranks[p.get_doc_id()] == len(useful_query):
                    accum.append((p.get_doc_id(),p))
        document_ranks = {}
        accum = sorted(accum, key = lambda x: -self._rank(x[1]))
        return accum
            
                    

    def _rank(self, posting):
        if posting.get_importance() != []:
            return len(posting.get_importance())* 1.27 * posting.get_tf()
        else:
            return posting.get_tf()



            
        #temp code to return single term query important query postings
        
           


        # for k, v in useful_query.items()[0]:
        #     for postings in v:
        #         p = Posting(eval(postings))
        #         possible_postings

    # def _help_binary_search(self, q):
        







        


