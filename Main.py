from Posting import Posting
import Indexer
from Url import Url
from Html_Reader import Html_Reader
from Query import Query
from flask import Flask
from merge import merge_total
import time
import heapq
# from Query import Query



if __name__ == "__main__":

    # reader = Html_Reader()
    # reader.read_master_for_id("indexes2/index_master.txt", "indexes2/index_master_final.txt")
    # Indexer.get_all_files('DEV/')
    # merge_total('indexes2/')
    # Indexer.index_index()
    # Indexer.incerement_index()

    stop_words_list = ['which', 'my', 'all', "when's", 'the', "you'd", 'from', 'be', 'down', 'until', 'by', 'only',
                       "we're",
                       "couldn't", 'your', 'her', 'should', 'but', 'at', 'having', 'ours', 'doing', "who's", 'during',
                       "i've",
                       'those', 'as', 'myself', 'than', 'himself', "i'm", 'very', 'this', "we'd", 'them', 'ourselves',
                       "doesn't",
                       'is', "we'll", "what's", 'had', 'there', "there's", 'a', 'yours', "he's", 'with', "you'll",
                       'these', 'does',
                       'into', 'not', "that's", "hadn't", "hasn't", "it's", 'she', "why's", 'me', 'against',
                       'yourselves', 'it',
                       "you're", "he'll", "here's", 'further', 'in', 'own', "i'll", "shouldn't", "they've", "aren't",
                       'do', 'itself',
                       "wasn't", 'then', "shan't", 'again', 'i', 'were', 'why', 'through', 'more', 'when', "where's",
                       'once', 'being',
                       'who', "she'll", 'under', 'no', "can't", 'other', "they'll", 'they', 'below', "won't", 'each',
                       'themselves',
                       'would', 'on', 'both', 'while', 'hers', 'herself', 'cannot', "she's", 'nor', 'over', 'where',
                       'you', "you've",
                       "how's", 'up', 'how', 'ought', "they'd", 'am', 'what', 'whom', 'above', "i'd", "let's", 'their',
                       'him', 'after',
                       'was', 'before', 'for', 'did', 'few', "we've", "she'd", 'to', 'because', 'an', 'and', 'he',
                       'same', 'theirs',
                       'yourself', 'too', "don't", 'could', "wouldn't", "mustn't", 'so', 'such', 'its', 'here', 'are',
                       'off', 'out',
                       "didn't", 'have', 'his', 'or', "isn't", 'that', 'of', 'our', 'we', 'has', 'if', 'between',
                       'most', 'some',
                       "they're", "weren't", 'about', 'any', "haven't", "he'd", 'been']

    stop_words = set()
    reader = Html_Reader()
    for word in stop_words_list:
        stop_words.add(reader.porter_stem(word))
    main = 'indexes2/'
    index_master = Indexer.index_index_object2(main + "index_index2.txt")
    page_rank = Indexer.page_rank(main + "pagerank.txt")
    doc_ids = Indexer.doc_ids(main + "doc_ids.txt")
    x = time.time()
    query = "master of software engineering"
    q = Query(query, index_master, page_rank, doc_ids, stop_words)
    important = q.retrieve_query()
    print('retrieve query', time.time()-x)
    with open(main + "doc_ids.txt", "r") as ids:
        mapping = eval(ids.readline())
    # print(important)
    words = set()
    print(len(important))
    for i in range(20):
        while important[0][1] in words:
            heapq.heappop(important)
        print(important[0][1], mapping[important[0][1]])
        words.add(important[0][1])
        heapq.heappop(important)
    # for i, y in enumerate(important[0:20]):
    #     print(i, mapping[y[1]], y[1]['cos_val'])
    print('end query', time.time() - x)
