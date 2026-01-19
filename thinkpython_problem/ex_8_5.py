
word = str(input("enter the word you wanna rotate:"))

n = int(input("by how much you wanna rotate it:"))

def rotate_word(word, n):
    result = ""
    for c in word:
        new_char = chr(ord(c) + n)
        result += new_char
    return result

            
print(rotate_word(word,n))