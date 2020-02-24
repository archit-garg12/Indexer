import os


def merge_two_files(file1: [str], file2: [str]) -> None:

    with open(file1, 'w') as f1, open(file2) as f2:
        next_line1 = 0
        next_line2 = 0
        while next_line1 < len(file1) and next_line2 != '':
            l1 = next_line1.split('#')
            l2 = next_line2.split('#')
            word1 = l1[0]
            word2 = l2[0]
            if word1 == word2:
                combined = eval(l1[1]) + eval(l2[1])
                f1.write(word1 + '#' + str(combined) + '#\n')
                next_line1 = f1.readline()
                next_line2 = f2.readline()
            elif word1 < word2:
                f1.write(word1 + '#' + l1[1] + '#\n')
                next_line1 = f1.readline()
            elif word2 < word1:
                f1.write(word2 + '#' + l2[1] + '#\n')
                next_line2 = f2.readline()
        while next_line1 != '':
            l1 = next_line1.split('#')
            word1 = l1[0]
            f1.write(word1 + '#' + l1[1] + '#\n')
            next_line1 = f1.readline()

        while next_line2 != '':
            l2 = next_line2.split('#')
            word2 = l2[0]
            f1.write(word2 + '#' + l2[1] + '#\n')
            next_line2 = f2.readline()

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


# merge_two_files('indexes/file1.txt', 'indexes/file2.txt', 'indexes/final.txt')






def merge_total(directory: str) -> None:
    listdir = os.listdir(directory)
    if len(listdir) == 1:
        return
    merge_two_files(directory + 'file1.txt', directory + 'file2.txt', directory + 'final1.txt')
    i = 2
    while len(os.listdir('indexes/')) > 1:
        merge_two_files(os.listdir('indexes/')[0], directory + 'final' + str(i-1) + '.txt', directory + 'final' + str(i) + '.txt')
        i += 1
        listdir = os.listdir('indexes/')


# # merge_total('indexes/')
# # print(os.listdir('indexes/'))
# x = open('indexes/file3.txt')
# print(x.readline(), type(x.readline()))
#
# print(x.readline() == '', 'jaksldfjlkas')
