from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
# from Query import Query



if __name__ == "__main__":

    # reader = Html_Reader()
    # reader.read_master_for_id("indexes/index_master.txt", "indexes/index_master_final.txt")
    # Indexer.get_all_files('DEV/')
    #merge_total('indexes/')
    # Indexer.index_index()
    mapping = {}
    reader = Html_Reader()
    query = "gays"
    query = reader.porter_stem(query)
    q = Query(query, Indexer.index_index_object())
    important = q.retrieve_query()

    with open("indexes/doc_ids.txt", "r") as ids:
        mapping = eval(ids.readline())
        
    for x in important:
        print(mapping[x])


    