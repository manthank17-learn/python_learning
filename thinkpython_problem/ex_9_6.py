"""
Think Python Chapter 9
Exercise 9-6

Write a function named is_abecedarian that returns True if the
letters in a word appear in alphabetical order (double letters allowed).

Then count how many abecedarian words are in the word list.
"""

def is_abecedarian(word):
    """
    Returns True if letters in word appear in alphabetical order.
    """
    word = word.lower()

    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


def count_abecedarian_words(filename):
    """
    Counts how many abecedarian words are in the given file.
    """
    count = 0

    with open(filename) as f:
        for line in f:
            word = line.strip()
            if is_abecedarian(word):
                count += 1

    return count


# Program starts here 
filename = "thinkpython_problem/word.txt"
result = count_abecedarian_words(filename)

print("Number of abecedarian words:", result)
