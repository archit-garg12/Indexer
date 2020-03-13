import os


def merge_two_files(master: str, file2: str) -> None:

    with open(master, 'r+') as m, open(file2) as f2:
        master_file = m.readlines()
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
            word2 = l2[0]
            m.write(word2 + '#' + l2[1] + '#\n')
            next_line2 += 1



def merge_total(directory: str) -> None:
    i = 1
    master_file = 'indexes2/index_master.txt'
    while i <= 44:
        merge_two_files(master_file, directory + 'inverted_index_' + str(i))
        i += 1
