import os


def merge_two_files(master: str, file2: str) -> None:

    with open(master, 'r+') as m, open(file2) as f2:
        master_file = m.readlines()
        # clear master file
        m.seek(0)
        m.truncate(0)
        compare_file = f2.readlines()
        next_line1 = 1
        next_line2 = 1
        while next_line1 < len(master_file)-1 and next_line2 < len(compare_file)-4:
            l1 = master_file[next_line1].split('#')
            l2 = compare_file[next_line2].split('#')
            word1 = l1[0]
            word2 = l2[0]
            if word1 == word2:
                combined = eval(l1[1]) + eval(l2[1])
                m.write(word1 + '#' + str(combined) + '#\n')
                next_line1 += 1
                next_line2 += 1
            elif word1 < word2:
                m.write(word1 + '#' + l1[1] + '#\n')
                next_line1 += 1
            elif word2 < word1:
                m.write(word2 + '#' + l2[1] + '#\n')
                next_line2 += 1
        while next_line1 < len(master_file)-1:
            l1 = master_file[next_line1].split('#')
            word1 = l1[0]
            m.write(word1 + '#' + l1[1] + '#\n')
            next_line1 += 1

        while next_line2 < len(compare_file)-4:
            l2 = compare_file[next_line2].split('#')
            # print(next_line2, len(compare_file)-1)
            word2 = l2[0]
            # print(l2)
            m.write(word2 + '#' + l2[1] + '#\n')
            next_line2 += 1

    # os.remove(file1)
    # os.remove(file2)


    # file 1
    # fish#[{doc_id:1, positions: [1,2,3,4]}, {doc_id:2, positions:[5,8,10]}]#\n
    # dog#[{doc_id:1, positions: [1,2,3,4]}, {doc_id:2, positions:[5,8,10]}]#\n
    # cat#[{doc_id:1, positions: [1,2,3,4]}, {doc_id:2, positions:[5,8,10]}]#\n
    #
    #
    # file 2
    # dog [{doc_id:5, positions: [1,2,3,4]}, {doc_id:6, positions:[5,8,10]}]\n
    # cat [{doc_id:5, positions: [1,2,3,4]}, {doc_id:6, positions:[5,8,10]}]\n
    # apple [{doc_id:5, positions: [1,2,3,4]}, {doc_id:6, positions:[5,8,10]}]\n

    # f1 = readline()
    # f2 = readline()
    # f1.word == f2.word:
    #     f1.list + f2.list
    #     increment f1 and f2
    # f1.word > f2.word:
    #     f2
    #     increment f2
    # f2.word > f1.word:
    #     f1
    #     increment f1


# merge_two_files('indexes/file1.txt', 'indexes/file2.txt')






def merge_total(directory: str) -> None:
    listdir = os.listdir(directory)
    # if len(listdir) == 1:
    #     return
    # merge_two_files(directory + 'file1.txt', directory + 'file2.txt', directory + 'final1.txt')
    i = 1
    master_file = 'indexes/index_master.txt'
    while i <= 55:
        print(i)
        merge_two_files(master_file, directory + 'inverted_index_' + str(i))
        print(i, 'DONE')
        i += 1

merge_total('indexes/')
# # merge_total('indexes/')
# # print(os.listdir('indexes/'))
# x = open('indexes/file3.txt')
# print(x.readline(), type(x.readline()))
#
# print(x.readline() == '', 'jaksldfjlkas')
