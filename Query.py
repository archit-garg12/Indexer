import os
from Posting import Posting
from collections import defaultdict
from Html_Reader import Html_Reader
import math


class Query():
    def __init__(self, query, index, page_rank, doc_ids):
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
        # page rank values
        self.page_rank = page_rank
        # doc id values
        self.doc_ids = doc_ids
        # print(index)
        self._tfidf_dict, self._total_tfidf = self._tfidf()
        print('QUERY', self.query)


    def cosine(self):
        tfidf_vector = self._tfidf()



    def retrieve_query(self):
        useful_query = {}
        doc_scores = {}
        words = {}

        # new
        # with open("indexes_old/index_master_final.txt", "r") as master:
        with open("indexes/index_master_final.txt", "r") as master:
            for word in self._tfidf_dict:
                freq = self._tfidf_dict[word][0] # frequency of word in query
                idf = self._tfidf_dict[word][1] # idf of word in query
                print(freq, idf)
                master.seek(self.index[word], 0)
                postings_list = eval(master.readline().split("#")[1])
                for posting in postings_list:
                    p = Posting(eval(posting))
                    curr_doc_id = p.get_doc_id()
                    curr_doc_tfidf = p.get_tfidf()
                    if curr_doc_id not in doc_scores:
                        doc_scores[curr_doc_id] = {
                            'cos_numer': 0,
                            'cos_denom': 0,
                            'importance': 0,
                            'link_val': 0
                        }
                    doc_scores[curr_doc_id]['cos_numer'] += (curr_doc_tfidf * freq * idf)
                    doc_scores[curr_doc_id]['cos_denom'] += (curr_doc_tfidf * curr_doc_tfidf)
                    doc_scores[curr_doc_id]['importance'] += len(p.get_importance())
                    if word.lower() in self.doc_ids[curr_doc_id].lower():
                        doc_scores[curr_doc_id]['link_val'] += idf
                    # if curr_doc_id in doc_scores:
                    #
                    #     doc_scores[curr_doc_id][3] +=
                    # else:
                    #     doc_scores[curr_doc_id] = [curr_doc_tfidf*freq*idf, curr_doc_tfidf*curr_doc_tfidf, 0, len(p.get_importance())]
                    # if word.lower() in self.doc_ids[curr_doc_id].lower():
                    #     doc_scores[curr_doc_id][2] += idf

        return sorted(doc_scores, key=lambda x: -self._rank(doc_scores[x], x))


        # old
        # with open("indexes/index_master_final.txt", "r") as master:
        #     print(self.query)
        #     # sort the query by idf first
        #     for word in self.query:
        #         #read each line and check if the first
        #         # {
        #         #     doc_id: {
        #         #         query_term1: tfidf,
        #         #         query_term2: tfidf
        #         #     }
        #         # }
        #         # {
        #         #     query_term1: [Postings],
        #         #     query_term2: [Postings]
        #         #
        #         # }
        #         if word in self.index:
        #             master.seek(self.index[word], 0)
        #             list_of_postings = eval(master.readline().split("#")[1])
        #             useful_query[word] = list_of_postings
        #             # loop through postings - store doc id's with tfidf
        # # {'learn': [2, 5.7244938513699575], 'machien': [1, 10.679066891449532]}
        #
        #
        #
        # # print(useful_query)
        # #sort dict by length of postings so process less posting lists first to easily determine overlap over multiple terms
        # useful_query = sorted(useful_query.items(), key = lambda x: len(x[1]))
        # document_ranks = defaultdict(int)
        # postings_collection = defaultdict(list)
        # accum = []
        # print(useful_query)
        # # userful query = {word: [postings]}
        # for lists in useful_query:
        #     for l in lists[1]:
        #         p = Posting(eval(l))
        #         document_ranks[p.get_doc_id()] += 1
        #         postings_collection[p.get_doc_id()].append(p)
        #         # only append postings
        #         if document_ranks[p.get_doc_id()] == len(useful_query):
        #             accum.append((p.get_doc_id(),postings_collection[p.get_doc_id()]))
        # # print([ (keys, document_ranks[keys])for keys in document_ranks if document_ranks[keys] ==  len(self.query)])
        # accum = sorted(accum, key = lambda x: -self._rank(x[1]))
        # return accum

    def _rank(self, doc_score, doc_id):
        # print((doc_score[0]/math.sqrt(self._total_tfidf*doc_score[1])))
        # return (doc_score[0]/math.sqrt(self._total_tfidf*doc_score[1]))
        final = 1
        # if importance > 0:
        #     # importance value
        #     final *= math.log(1 + importance)
        # cosine value
        final *= (doc_score['cos_numer']/math.sqrt(self._total_tfidf*doc_score['cos_denom']))
        # print(doc_score['link_val'])
        if doc_score['importance'] > 0:
            final += math.log(1 + doc_score['importance'])
        if doc_score['link_val'] > 0:
            final += math.log(1 + doc_score['link_val'])
        # # page rank value
        # # final /= page_rank
        # final += self.page_rank[doc_id]
        return final

    # def _in_url(self):


    def _tfidf(self):
        # words = {}
        # total_idf = 0.0
        # with open("indexes_old/index_master_final.txt", "r") as master, open('indexes_old/index_master.txt', 'r') as master2:
        #     for word in self.query:
        #         if word in self.index:
        #             if word in words:
        #                 count = words[word][0]
        #                 idf = words[word][1]
        #                 new_count = count + 1
        #                 total_idf -= (count*count*idf*idf)
        #                 words[word][0] = new_count
        #                 total_idf += (new_count*new_count*idf*idf)
        #             else:
        #                 master.seek(self.index[word], 0)
        #                 master2.seek(self.index2[word], 0)
        #                 x = eval(eval(master.readline().split('#')[1])[0])['tfidf']
        #                 tfidf = float(x)
        #                 # print(eval(eval(master2.readline().split('#')[1])[0]))
        #                 tf = float(eval(eval(master2.readline().split('#')[1])[0])['tf'])
        #                 print(tf)
        #                 idf = tfidf/tf
        #                 words[word] = [1, idf]
        #                 total_idf += (idf*idf)
        # return words, total_idf

        words = {}
        total_idf = 0.0
        with open("indexes/index_master_final.txt", "r") as master:
            for word in self.query:
                if word in self.index:
                    if word in words:
                        count = words[word][0]
                        idf = words[word][1]
                        new_count = count + 1
                        total_idf -= (count*count*idf*idf)
                        words[word][0] = new_count
                        total_idf += (new_count*new_count*idf*idf)
                    else:
                        master.seek(self.index[word], 0)
                        # print(master.readline().split('#')[1])
                        idf = float(master.readline().split('#')[2])
                        words[word] = [1, idf]
                        total_idf += (idf*idf)
        return words, total_idf
    #
    # def _cosine_val(self, doc_vector: {str: float}, query_vector: {str: float}):
    #     loop_length = len(doc_vector)
    #     denom = 0
    #     numer = 0
    #     for key, value in query_vector:
    #         denom += (value * doc_vector[key])
    #
    #     return denom/numer
                    

    # def _rank(self, posting):
    #     accum = 0
    #     for p in posting:
    #         # if p.get_importance() != []:
    #         #     accum += math.log(10 + len(p.get_importance())) * p.get_tfidf()
    #         # else:
    #         accum += p.get_tfidf()
    #     return accum



            
        #temp code to return single term query important query postings
        
           


        # for k, v in useful_query.items()[0]:
        #     for postings in v:
        #         p = Posting(eval(postings))
        #         possible_postings

    # def _help_binary_search(self, q):
        







        


