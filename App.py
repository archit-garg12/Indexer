from flask import Flask
from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
from flask_restful import Resource, Api
from flask_cors import CORS
import time
from heapq import heappop

app = Flask(__name__)
CORS(app)
api = Api(app)
index = Indexer.index_index_object2(2)
page_rank = Indexer.page_rank()
mapping = Indexer.doc_ids()
current_heap = 0

stop_words_list = ['which', 'my', 'all', "when's", 'the', "you'd", 'from', 'be', 'down', 'until', 'by', 'only', "we're",
              "couldn't", 'your', 'her', 'should', 'but', 'at', 'having', 'ours', 'doing', "who's", 'during', "i've",
              'those', 'as', 'myself', 'than', 'himself', "i'm", 'very', 'this', "we'd", 'them', 'ourselves', "doesn't",
              'is', "we'll", "what's", 'had', 'there', "there's", 'a', 'yours', "he's", 'with', "you'll", 'these', 'does',
              'into', 'not', "that's", "hadn't", "hasn't", "it's", 'she', "why's", 'me', 'against', 'yourselves', 'it',
              "you're", "he'll", "here's", 'further', 'in', 'own', "i'll", "shouldn't", "they've", "aren't", 'do', 'itself',
              "wasn't", 'then', "shan't", 'again', 'i', 'were', 'why', 'through', 'more', 'when', "where's", 'once', 'being',
              'who', "she'll", 'under', 'no', "can't", 'other', "they'll", 'they', 'below', "won't", 'each', 'themselves',
              'would', 'on', 'both', 'while', 'hers', 'herself', 'cannot', "she's", 'nor', 'over', 'where', 'you', "you've",
              "how's", 'up', 'how', 'ought', "they'd", 'am', 'what', 'whom', 'above', "i'd", "let's", 'their', 'him', 'after',
              'was', 'before', 'for', 'did', 'few', "we've", "she'd", 'to', 'because', 'an', 'and', 'he', 'same', 'theirs',
              'yourself', 'too', "don't", 'could', "wouldn't", "mustn't", 'so', 'such', 'its', 'here', 'are', 'off', 'out',
              "didn't", 'have', 'his', 'or', "isn't", 'that', 'of', 'our', 'we', 'has', 'if', 'between', 'most', 'some',
              "they're", "weren't", 'about', 'any', "haven't", "he'd", 'been']


stop_words = set()
reader = Html_Reader()
for word in stop_words_list:
    stop_words.add(reader.porter_stem(word))


class QueryRequest(Resource):

     def get(self, query):
        l = []
        global current_heap
        q = Query(query, index, page_rank, mapping, stop_words)
        start = time.time()
        current_heap = q.retrieve_query()
        end = time.time()
        for x in range(50):
            try:
                l.append(mapping[current_heap[0][1]])
                heappop(current_heap)
            except:
                break
        final = end - start
        return {query: l, "time": final}

class UpdateQuery(Resource):
    def get(self, amount):
        l = []
        global current_heap
        for x in range(amount):
            try:
                l.append(mapping[current_heap[0][1]])
                heappop(current_heap)
            except:
                break
        return {"data": l}




api.add_resource(QueryRequest, '/<string:query>')
api.add_resource(UpdateQuery, '/next/<int:amount>')

