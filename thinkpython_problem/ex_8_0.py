fruit = "banana"
lenght = len(fruit)

"""
index = 0
while index <len(fruit):
    letter = fruit[index]
    print(letter)
    index = index +1
"""
def print_backward(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1
print_backward("manthan") 
        

