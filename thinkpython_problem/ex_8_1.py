fruit = 'banana'
suffix = 'ack'

for letter in fruit:
    print(letter + suffix)

"""
we have ex 8.1.py\

goal:
-learn string methods by expriremental use
-understand optional arguments
-build intution by running code


"""

text = " hello python  "
print(text.strip())

print(text.lstrip()) # left only        
print(text.rstrip()) # right only

s = "banana"
print(s.replace("a","o"))

name = "manthan"
print(name.find("a",2,5))
