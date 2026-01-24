
word = input("Enter a word: ").strip().lower()
allowed = input("Enter allowed letters: ").strip().lower()

def uses_only(word, allowed):
    for ch in word:
        if ch not in allowed:
            return False
    return True

if uses_only(word, allowed):
    print("The word uses only the allowed letters.")
else:
    print("The word uses letters not allowed.")