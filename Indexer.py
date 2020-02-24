import json
import os
from collections import defaultdict
from Url import Url
from Html_Reader import Html_Reader


DOC_ID_DICT = dict()


def get_all_files(dev_directory):

    file_count_name = 'indexes/inverted_index_1'
    file_count = 0
    file_count_name_count = 1
    doc_id = 0
    inverted_index = defaultdict(list)
    reader = Html_Reader()
    for direct in os.listdir(dev_directory):

        if direct != '.DS_Store':

            for file in os.listdir(dev_directory + direct):
                try:
                    doc_id += 1
                    # posting(file) returns url and stuff for DOC_ID_DICT and for tokenizer
                    temp = Url(dev_directory + direct + '/' + file)
                    print(dev_directory + direct + '/' + file)
                    # write to a file the current inverted index, if it is above a certain file count
                    if file_count >= 50:
                        with open(file_count_name, 'w+') as count:
                            count.write('{\n')
                            s = sorted(inverted_index.items(), key=lambda x: x[0])
                            for k, v in s:
                                count.write(str(k) + '#' + str([str(x) for x in v]) + '#\n')
                            count.write('}')
                        file_count_name_count += 1
                        file_count = 0
                        file_count_name = file_count_name[:-1] + str(file_count_name_count)
                        # adds the current dict to a file for a partial index
                        # change file_count_name also to write to a different file
                    reader.read_file(temp.get_html(), doc_id, inverted_index)
                    DOC_ID_DICT[doc_id] = temp.get_url()
                except Exception as e:
                    with open('error.txt', 'a+') as error_file:
                        error_file.write(str(e) + str(temp))


def test():
    # for file in os.listdir('DEV/aiclub_ics_uci_edu'):
    #     print(file)
    x = dict()
    file_count_name = 'indexes/inverted_index_1'

    inv = defaultdict(list)
    temp = Url('DEV/www_cs_uci_edu/f1a7ab7fb645fe5df395bac24cb4a09d8e8c239b5b0ec10783ec7381d8f7125e.json')
    print('penis lover 3000')
    reader = Html_Reader()
    print('fuck you krish')
    reader.read_file(temp.get_html(), 1, inv)
    print('krish doesnt like us anymore')
    # print(str(inv["ami"][0]))
    with open(file_count_name, 'w+', encoding = 'utf-8') as count:
        count.write('{\n')
        s = sorted(inv.items(), key=lambda x: x[0])
        for k, v in s:
            print([x for x in v])
            count.write(str(k) + '#' +  str([str(x) for x in v]) + '#\n')
        count.write('}')
    with open('indexes/data.json', 'w') as fp:
        for k,v in inv.items():
            temp = {}
            temp[k] = [c.__dict__ for c in v]
            json.dump(temp , fp)


if __name__ == '__main__':
    #get_all_files('DEV/')
    test()
