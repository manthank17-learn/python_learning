word_file = open('thinkpython_problem\word.txt')

def has_no_e(word):
      for ch in word:
            if ch == 'e' or ch == 'E':
               return False
      return True

for line in word_file:
     word = line.strip()
     if has_no_e(word):
          print(word)      
