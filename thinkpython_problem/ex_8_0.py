fruit = "banana"
lenght = len(fruit)

"""
index = 0
while index <len(fruit):
    letter = fruit[index]
    print(letter)
    index = index +1
"""
"""
def print_backward(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1
print_backward("manthan") 
        
"""
"""
s = "monty python"
print(s[0:5])
print(fruit[::-1])

new_fruit = 'm' +fruit[1:]
print(new_fruit)


"""

"""
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1

    return -1

print(find ( fruit,'a'))
"""


def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(find(fruit, 'a', 2))


def count(word,letter,start):
    count = 0
    index = start
    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1
    return count

print(count(fruit,'a',4))

print(fruit.upper())


def in_both(word1, word2): 
    for letter in word1: 
        if letter in word2: 
            print(letter)


print(in_both('manthan', 'man'))

