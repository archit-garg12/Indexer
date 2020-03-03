from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
from flask import Flask
# from Query import Query



if __name__ == "__main__":

    # reader = Html_Reader()
    # reader.read_master_for_id("indexes/index_master.txt", "indexes/index_master_final.txt")
    # Indexer.get_all_files('DEV/')
    #merge_total('indexes/')
    # Indexer.index_index()
    # Indexer.incerement_index()
    index = Indexer.index_index_object2()
    mapping = {}
    query = "acm"
    q = Query(query, index)
    important = q.retrieve_query()
    with open("indexes/doc_ids.txt", "r") as ids:
        mapping = eval(ids.readline())

    print(important)
    for x in important[0:5]:
        print(mapping[x[0]])
        for p in x[1]:
            print(p.get_doc_id())


