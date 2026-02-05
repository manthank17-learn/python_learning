word1= str(input("whats the first word?:"))
word2=str(input("whats the second word?:"))

def is_anagram(w1,w2):
    l1 = list(w1)
    l2 = list(w2)

    l1.sort()
    l2.sort()

    return l1 == l2 

print(is_anagram(word1,word2))