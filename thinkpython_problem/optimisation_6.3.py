
word = str(input("enter your word G?"))

def is_palindorme(word):

    if word[::-1] == word:
       return 1
    
    else:
        return 0

print(is_palindorme(word))
