"""
Docstring for thinkpython_problem.ex_9_0

-goal to practice the previous concepts till chapter 8
-build intution by solving problems
-learn to debug code
-learn to optimize code
"""

"""
revising 
-loop
-len()
-string handling 
"""
word = [
        "banana",
        "apple",
        "extraordinary",
        "pneumonoultramicroscopicsilicovolcanoconiosis",
        "hi"
        ]
for w in word:
    print(w) # print each work in the word list
print("---------------------------------")

for w in word:
    print(w, len(w)) # print each word with its length
print("---------------------------------")

# applying conditions
for word in word:
    if len(word) >10:
        print(word)
print("---------------------------------")


# wraping in a function
def print_long_words(word):
    for word in word:
        if len(word) >20:
            print(word)
print("---------------------------------")

print_long_words(word)
print("---------------------------------")