import json
import os
from collections import defaultdict
from Url import Url


DOC_IC_DICT = dict()


def get_all_files(dev_directory):

    file_count_name = 'indexes/inverted_index_1'
    file_count = 0
    file_count_name_count = 1
    doc_id = 0
    inverted_index = defaultdict(list)

    for direct in os.listdir(dev_directory):

        if direct != '.DS_Store':

            for file in os.listdir(dev_directory + direct):
                doc_id += 1
                # posting(file) returns url and stuff for DOC_ID_DICT and for tokenizer
                temp = Url(dev_directory + direct + '/' + file)
                print(file)
                # write to a file the current inverted index, if it is above a certain file count
                if file_count >= 50:
                    # with open(file_count_name, 'a+') as count:
                    # count.write('{\n')
                    # s = sorted(inverted_index.items(), key=lambda x: x[0])
                    # for k, v in s:
                    #     count.write(str(k) + ':' + str(v) + ',\n')
                    # count.write('}')
                    # file_count_name_count += 1
                    # file_count_name = file_count_name[:-1] + str(file_count_name_count)
                    # adds the current dict to a file for a partial index
                    # change file_count_name also to write to a different file
                    pass
                # temp = posting(temp.get_url(),doc_id)
                # Html_Reader(temp)
                # DOC_IC_DICT[doc_id] = temp
                # for k, v in temp.inverted_index.items():
                #     inverted_index[k].append(v)


def test():
    # for file in os.listdir('DEV/aiclub_ics_uci_edu'):
    #     print(file)
    x = dict()
    temp = Url('DEV/aiclub_ics_uci_edu/8ef6d99d9f9264fc84514cdd2e680d35843785310331e1db4bbd06dd2b8eda9b.json')
    print(temp.get_url())


if __name__ == '__main__':
    # get_all_files('DEV/')
    test()
