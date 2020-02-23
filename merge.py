import os


def merge_two_files(file1: str, file2: str, write_file: str) -> None:
    with open(file1) as f1, open(file2) as f2, open(write_file, 'w+') as w:
        for p1, p2 in zip(f1, f2):
            line_split = p1.split()
            word = line_split[0]
            postings = eval(line_split[1])
            postings2 = eval(p2.split()[1])
            postings += postings2
            write_file.write(word + ' ' + str(postings))
    os.remove(file1)
    os.remove(file2)


def merge_total(directory: str) -> None:
    listdir = os.listdir(directory)
    if len(listdir) == 1:
        return
    merge_two_files(directory + 'file1.txt', directory + '/file2.txt', directory + 'final1.txt')
    while len(listdir) > 1:
        merge_two_files(listdir[0], directory + 'final' + str(i-1) + '.txt', directory + 'final' + str(i) + '.txt')


merge_total('indexes/')