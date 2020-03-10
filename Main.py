from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
from flask import Flask
import time
# from Query import Query



if __name__ == "__main__":

    # reader = Html_Reader()
    # reader.read_master_for_id("indexes/index_master.txt", "indexes/index_master_final.txt")
    # Indexer.get_all_files('DEV/')
    #merge_total('indexes/')
    # Indexer.index_index()
    # Indexer.incerement_index()



    # index_master = Indexer.index_index_object2(2)
    # index_master2 = Indexer.index_index_object2(3)
    # mapping = {}
    # query = "machine learning"
    # q = Query(query, index_master, index_master2)
    # # print(q.tfidf())
    # important = q.retrieve_query()
    # with open("indexes_old/doc_ids.txt", "r") as ids:
    #     mapping = eval(ids.readline())
    # for x in important[0:20]:
    #     print(mapping[x])
    #     print(x)
    index_master = Indexer.index_index_object2(2)
    # print('index index', time.time()-x)
    page_rank = Indexer.page_rank()
    # print('page rank', time.time()-x)
    doc_ids = Indexer.doc_ids()
    # print('doc ids', time.time()-x)
    x = time.time()
    # index_master2 = {}
    mapping = {}
    query = "master of software engineering"
    q = Query(query, index_master, page_rank, doc_ids)
    print('initialize query', time.time()-x)
    important = q.retrieve_query()
    print('retrieve query', time.time()-x)
    with open("indexes/doc_ids.txt", "r") as ids:
        mapping = eval(ids.readline())
    for i, y in enumerate(important[0:100]):
        print(i, mapping[y])
    print('end query', time.time() - x)

    # index = Indexer.index_index_object2()
    # mapping = {}
    # query = "cristina lopes"
    # q = Query(query, index)
    # # print(q.tfidf())
    # important = q.retrieve_query()
    # with open("indexes/doc_ids.txt", "r") as ids:
    #     mapping = eval(ids.readline())
    #
    # print(important)
    # for x in important[0:5]:
    #     print(mapping[x[0]])
    #     for p in x[1]:
    #         print(p.get_doc_id())