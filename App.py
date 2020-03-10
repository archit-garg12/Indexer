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

class QueryRequest(Resource):

     def get(self, query):
        l = []
        global current_heap
        q = Query(query, index, page_rank, mapping)
        start = time.time()
        current_heap = q.retrieve_query()
        print(" djas;jdas;kdjaskdjsaldkjaslkdsajdlsadjsaldj",current_heap)
        end = time.time()
        for x in range(50):
            try:
                l.append(mapping[current_heap[0][1]])
                heappop(current_heap)
            except:
                break
        final = end- start
        return {query: l, "time": final}\

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

