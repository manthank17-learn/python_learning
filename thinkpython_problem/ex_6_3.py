word= str(input("what is your word G?:"))

def is_palindrome(word):
    n = len(word)
    i = 0

    while i < n // 2:
        first = word[i]
        last = word[-(i + 1)]

        if first != last:
            return False

        i += 1

    return True

print(is_palindrome(word))