from flask import Flask
from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
from flask_restful import Resource, Api
from flask_cors import CORS
import time
app = Flask(__name__)
CORS(app)
api = Api(app)
index = Indexer.index_index_object2()
with open("indexes/doc_ids.txt", "r") as ids:
    mapping = eval(ids.readline())

class QueryRequest(Resource):
     def get(self, query):
        l = []
        q = Query(query, index)
        start = time.time()
        important = q.retrieve_query()
        end = time.time()
        for x in important:
            l.append(mapping[x[0]]) 
        final = start-end
        return {query: l, time: final}

api.add_resource(QueryRequest, '/<string:query>')

