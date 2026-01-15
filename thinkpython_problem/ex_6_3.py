word =str(input("whats the word G??"))

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(last(word),middle(word),first(word))