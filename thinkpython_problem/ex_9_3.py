def avoids(word, forbidden):
    for ch in word:
        if ch in forbidden:
            return False
    return True


forbidden = input("Enter forbidden letters: ").strip().lower()
filename = "thinkpython_problem/word.txt"

count = 0

with open(filename) as f:
    for line in f:
        word = line.strip().lower()
        if avoids(word, forbidden):
            count += 1

print("Number of words without forbidden letters:", count)
