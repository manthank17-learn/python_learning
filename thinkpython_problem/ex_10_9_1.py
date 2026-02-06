filename = r"C:\Users\rayuser\Documents\python-core\thinkpython_problem\word.txt"

def read_words_append(filename):
    words = []                     # empty list

    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()    # remove \n
            words.append(word)     # add element

    return words

print(read_words_append(filename))