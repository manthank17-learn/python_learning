import math
"""
- b**a, if a%b==0
-b**(a/b)

def is_power(a,b):

return bool
"""
a = int(input("enter value of a ?:"))
b = int(input("enter value of the b:"))

def is_power(a, b):
    if a == b:
        return True
    if a < b or a % b != 0:
        return False
    return is_power(a // b, b)

print(is_power(a,b))