"""
Think PythonChapter 9
Exercise 9_5 (User Input Version)

User enters multiple words.
Program counts how many words use all vowels (aeiou).
"""

def uses_all(word, required):
    """
    Returns True if word contains all required letters at least once.
    """
    for ch in required:
        if ch not in word:
            return False
    return True


#Collect words from user

words = []
print("Enter words one by one. Type 'done' to finish.")

while True:
    w = input("Word: ").strip().lower()
    if w == "done":
        break
    words.append(w)

#Check vowel
required_letters = "aeiou"
count = 0
for word in words:
    if uses_all(word, required_letters):
        count += 1

print("Number of words that use all vowels (aeiou):", count)
