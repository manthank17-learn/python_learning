 
word = open('thinkpython_problem\word.txt')

def  get_each_word(word):
         for w in word:
            print(w) # i wanna store the value of each w here and use that in the next function 

def check_for_e(w):
      e = chr(101)
      E = chr(69)
      for e in w:
            if ord(e) == e or ord(e)== E :
                  print("True")
            else:
                  print("false")

print(check_for_e(w))                 
    
"""
e = chr(101)
E = chr(69)

def has_no_e(word):
   for i in word:
      if ord(i) == ord(e) :
        print("true")
      elif ord(i) == ord(E):
         print("true")  
      else:
         False 

has_no_e(word)     
"""