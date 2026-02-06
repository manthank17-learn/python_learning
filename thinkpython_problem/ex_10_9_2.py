filename = r"C:\Users\rayuser\Documents\python-core\thinkpython_problem\word.txt"
def read_words_plus(filename):
    words = []

    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            words = words + [word]

    return words

print(read_words_plus(filename))