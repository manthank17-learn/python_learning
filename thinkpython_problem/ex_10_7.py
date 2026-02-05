word = str(input("whats the word:?"))

def  has_dupli(word):
    l1 = list(word)
    for i in range(len(l1)):
            for j in range(i+1,len(l1)):
                  if l1[i] == l1[j]:
                    return True
    return False
      
print(has_dupli(word))
            
                     
