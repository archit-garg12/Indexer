import json
import os
from collections import defaultdict
from Url import Url
from Html_Reader import Html_Reader


DOC_ID_DICT = dict()


def get_all_files(dev_directory):

    file_count_name = 'indexes/inverted_index_'
    file_count = 0
    file_count_name_count = 1
    doc_id = 1
    inverted_index = defaultdict(list)
    reader = Html_Reader()
    for direct in os.listdir(dev_directory):

        if direct != '.DS_Store':

            for file in os.listdir(dev_directory + direct):
                
                # print(doc_id)
                # posting(file) returns url and stuff for DOC_ID_DICT and for tokenizer
                temp = Url(dev_directory + direct + '/' + file)
                print(dev_directory + direct + '/' + file)
                try:
                    read = reader.read_file(temp.get_html(), doc_id, inverted_index)
                    print(read)
                    if read:
                        print(doc_id)
                        # write to a file the current inverted index, if it is above a certain file count
                        file_count += 1
                        DOC_ID_DICT[doc_id] = temp.get_url()
                        doc_id += 1

                except Exception as e:
                    with open('error.txt', 'w+') as error_file:
                        error_file.write(str(e) + str(temp.get_url()) + "\n")
                if file_count == 1000:
                    write_to_index(inverted_index, file_count_name_count, file_count_name)
                    inverted_index = defaultdict(list)
                elif file_count > 1000:
                    file_count_name_count += 1
                    file_count = 0
                    # adds the current dict to a file for a partial index
                    # change file_count_name also to write to a different file
                
    write_to_index(inverted_index, file_count_name_count,file_count_name)
    write_doc_ids(DOC_ID_DICT)        

def write_doc_ids(ids):
    with open("doc_ids.txt", "w+") as id:
        id.write(str(ids))

def write_to_index(inverted_index, file_count_name_count, file_count_name):
     with open(file_count_name + str(file_count_name_count), 'w+') as count:
        count.write('{\n')
        s = sorted(inverted_index.items(), key=lambda x: x[0])
        for k, v in s:
            count.write(str(k) + '#' + str([str(x) for x in v]) + '#\n')
        count.write('}')
        count.write('\n\n\n\n')

def index_index():
    alpha = {}
    with open('indexes/index_master_final.txt', "r") as master:
        seek = 0
        for lines in master:
            line = lines.split("#")
            alpha[line[0]] = seek
            seek += len(lines)
    with open("indexes/index_index2.txt", "w+") as i:
        i.write(str(alpha))
def index_index_object2():
    with open("indexes/index_index2.txt", "r") as i:
        alpha = eval(i.readline().strip("\n"))
    return alpha
def incerement_index():
    fin = {}
    with open("indexes/doc_ids.txt", "r") as ids:
        with open("doc_ids.txt", "w+") as final:
            p = eval(ids.readline())
            for x in p:
                fin[x-1] = p[x]
            final.write(str(fin))


def test():
    # for file in os.listdir('DEV/aiclub_ics_uci_edu'):
    #     print(file)
    x = dict()
    file_count_name = 'indexes/inverted_index_1'

    inv = defaultdict(list)
    temp = Url('DEV/aiclub_ics_uci_edu/8ef6d99d9f9264fc84514cdd2e680d35843785310331e1db4bbd06dd2b8eda9b.json')
    reader = Html_Reader()
    reader.read_file(temp.get_html(), 1, inv)
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
