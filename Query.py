import os
class Query():
    def __init__(self, query, index):
        temp = []
        for c in query.strip("\n").lower():
            char_number = ord(c)
            if (48 <= char_number <= 57) or (97 <= char_number <= 122):
                temp.append(c)
            else:
                temp.append(" ")
        #prepped query to process using tokenization method
        self.query = "".join(temp).split(" ")
        #index is the ranges of letters to seek postions
        self.index = index
    def retrieve_query(self):
        useful_query = {}
        with open("indexes/index_master.txt", "r") as master:
            print(self.query)
            for words in self.query:
                #for each word limits range to first letter of word
                curr = self.index[words[0]]
                seek = curr
                final = chr(ord(words[0]) + 1)
                if words[0] == "9":
                    final = "z"
                if words[0] == "z":
                    final = "end"
                final = self.index[final]
                # mid = int((curr + final)/2)
                master.seek(curr, 0)
                #read each line and check if the first 

                while seek < final:
                    # s = master.readline()
                    line = master.readline()
                    # mid = master.tell()
                  
                    lines = line.strip("\n").split("#")
                    seek += len(line)

                    if lines[0] == words:
                        useful_query[words] = eval(lines[1])
                        break
                    # elif lines[0] > words:
                    #     final = mid
                    #     mid = int((mid + curr)/2)
                    # elif lines[0] < words:
                    #     curr = mid
                    #     mid = int((mid + final)/2)
        # print(useful_query)
        #sort dict by length of postings so process less posting lists first to easily determine overlap over multiple terms
        useful_query = dict(sorted(useful_query.items(), key = lambda x: len(x[1])))

        #temp code to return single term query important query postings
        val = []
        for k in useful_query:
            for v in useful_query[k]:
                val.append(eval(v)['doc_id'])
        return val
        # for k, v in useful_query.items()[0]:
        #     for postings in v:
        #         p = Posting(eval(postings))
        #         possible_postings

    # def _help_bin(self, q):
    #     mid = len()







        


