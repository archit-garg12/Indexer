import os
from Posting import Posting
from collections import defaultdict
from Html_Reader import Html_Reader
import math


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
        print('QUERY', self.query)




    def cosine(self):
        tfidf_vector = self._tfidf()



    def retrieve_query(self):
        useful_query = {}
        with open("indexes/index_master_final.txt", "r") as master:
            # print(self.query)
            # sort the query by idf first
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
                if words in self.index:
                    master.seek(self.index[words], 0)
                    print(words)
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
        postings_collection = defaultdict(list)
        accum = []
        print(useful_query)
        # userful query = {word: [postings]}
        for lists in useful_query:
            for l in lists[1]:
                p = Posting(eval(l))
                document_ranks[p.get_doc_id()] += 1
                postings_collection[p.get_doc_id()].append(p)
                # only append postings
                if document_ranks[p.get_doc_id()] == len(useful_query):
                    accum.append((p.get_doc_id(),postings_collection[p.get_doc_id()]))
        # print([ (keys, document_ranks[keys])for keys in document_ranks if document_ranks[keys] ==  len(self.query)])
        accum = sorted(accum, key = lambda x: -self._rank(x[1]))
        return accum


    def _tfidf(self):
        words = {}
        with open("indexes/index_master_final.txt", "r") as master:
            for word in self.query:
                if word in self.index:
                    # add the value by the factor of
                    if word in words:
                        original_idf = words[word][1]/words[word][0]
                        words[word][0] += 1
                        words[word][1] = original_idf*words[word][0]
                    else:
                        master.seek(self.index[word], 0)
                        idf = float(master.readline().split('#')[2])
                        words[word] = [1, idf]
        return words

    def _cosine_val(self, doc_vector: {str: float}, query_vector: {str: float}):
        loop_length = len(doc_vector)
        denom = 0
        numer = 0
        for key, value in query_vector:
            denom += (value * doc_vector[key])

        return denom/numer
                    

    def _rank(self, posting):
        accum = 0
        for p in posting:
            if p.get_importance() != []:
                accum += math.log(10 + len(p.get_importance())) * p.get_tfidf()
            else:
                accum += p.get_tfidf()
        return accum



            
        #temp code to return single term query important query postings
        
           


        # for k, v in useful_query.items()[0]:
        #     for postings in v:
        #         p = Posting(eval(postings))
        #         possible_postings

    # def _help_binary_search(self, q):
        







        


