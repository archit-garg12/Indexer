import os
from Posting import Posting
from collections import defaultdict
from Html_Reader import Html_Reader
import math
import time
import heapq


class Query():
    def __init__(self, query, index, page_rank, doc_ids, stop_words):
        reader = Html_Reader()
        temp = []
        for c in query.strip("\n").lower():
            char_number = ord(c)
            if (48 <= char_number <= 57) or (97 <= char_number <= 122):
                temp.append(c)
            else:
                temp.append(" ")
        # prepped query to process using tokenization method
        self.query = []
        self.total_words = []
        total_count = 0
        stop_words_count = 0
        for x in "".join(temp).split(" "):
            word = reader.porter_stem(x)
            total_count += 1
            self.total_words.append(word)
            if word in stop_words:
                stop_words_count += 1
            else:
                self.query.append(word)
        if float(stop_words_count) / float(total_count) > 0.7:
            self.threshold = 100
            self.query = self.total_words
        else:
            self.threshold = 784

        # index is the ranges of letters to seek postions
        self.index = index

        # page rank values
        self.page_rank = page_rank

        # doc id values
        self.doc_ids = doc_ids

        # setup
        self._tfidf_dict, self._total_tfidf = self._setup()

        print(self.query)

    def retrieve_query(self):

        doc_scores = {}
        accum = []
        heapq.heapify(accum)
        with open("indexes2/index_master_final.txt", "r") as master:
            print(self._tfidf_dict)
            for word in self._tfidf_dict:
                count = 0
                freq = self._tfidf_dict[word][0] # frequency of word in query
                idf = self._tfidf_dict[word][1] # idf of word in query
                master.seek(self.index[word], 0)
                postings_list = eval(master.readline().split("#")[1])
                for posting in postings_list:
                    if count > self.threshold:
                        break
                    p = Posting(eval(posting))
                    curr_doc_id = p.get_doc_id()
                    curr_doc_tfidf = p.get_tfidf()
                    if curr_doc_id not in doc_scores:
                        doc_scores[curr_doc_id] = {
                            'cos_numer': 0,
                            'cos_denom': 0,
                            'cos_val': 0,
                            'importance': 0,
                            'link_val': 0
                        }
                    doc_val = doc_scores[curr_doc_id]
                    doc_scores[curr_doc_id]['cos_numer'] += (curr_doc_tfidf * freq * idf)
                    doc_scores[curr_doc_id]['cos_denom'] += (curr_doc_tfidf * curr_doc_tfidf)
                    doc_scores[curr_doc_id]['cos_val'] = (doc_val['cos_numer']/math.sqrt(self._total_tfidf*doc_val['cos_denom']))
                    doc_scores[curr_doc_id]['importance'] += p.get_importance()
                    if word.lower() in self.doc_ids[curr_doc_id].lower():
                        doc_scores[curr_doc_id]['link_val'] += idf
                    count += 1
                    heapq.heappush(accum, (-self._rank(doc_val, curr_doc_id), curr_doc_id))
                # print(word, time.time()-x, self._tfidf_dict[word])
        return accum
        # return sorted(doc_scores.items(), key=lambda x: -self._rank(x[1], x[0]))

    def _rank(self, doc_score, doc_id):
        # cosine value
        final = doc_score['cos_val']

        # importance value
        final += math.log(1 + doc_score['importance'])

        # link value
        final += math.log(1 + doc_score['link_val'])/2

        # page rank value
        final += self.page_rank[doc_id]*100

        return final

    def _setup(self):
        words = {}
        total_idf = 0.0
        query_list = []
        with open("indexes2/index_master_final.txt", "r") as master:
            for word in self.query:
                if word in self.index:
                    query_list.append(word)
                    if word in words:
                        count = words[word][0]
                        idf = words[word][1]
                        new_count = count + 1
                        total_idf -= (count*count*idf*idf)
                        words[word][0] = new_count
                        total_idf += (new_count*new_count*idf*idf)
                    else:
                        # setup line
                        master.seek(self.index[word], 0)
                        line = master.readline().split('#')

                        # idf processing
                        idf = float(line[2])
                        words[word] = [1, idf]
                        total_idf += (idf*idf)
        return words, total_idf
