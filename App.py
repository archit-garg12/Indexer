from flask import Flask
from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
index = Indexer.index_index_object2()
with open("indexes/doc_ids.txt", "r") as ids:
    mapping = eval(ids.readline())
query = "machine learning"

class QueryRequest(Resource):
     def get(self, query):
        l = []
        q = Query(query, index)
        important = q.retrieve_query()
        for x in important:
            l.append(mapping[x[0]]) 
        return {query: l}

api.add_resource(QueryRequest, '/<string:query>')

