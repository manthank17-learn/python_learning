for word in open("thinkpython_problem/word.txt"):
    word = word.strip()
    if 'e' not in word and 'E' not in word:
        print(word)