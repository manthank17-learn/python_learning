import math
"""def area(radius):
    a = math.pi * radius**2
    return a
"""
radius = int(input("what is the radius G?"))

x = int(input("what is the first number u wanna compare?"))
y= int(input("what is the second number u wanna compare?"))
z =int (input("what is your Z?"))
def area(radius):
    return math.pi * radius**2

print(area(radius))

"""

def compare(x,y):
    if x > y:
        return 1 
    elif x == y:
        return 0
    elif x < y:
        return -1

print(compare(x,y))
"""

def hypo(x,y):
     squaredV = x**2 + y**2
     return math.sqrt(squaredV)

print(hypo(x,y))


def is_bet(x,y,z):
     return bool(x<=y<=z)

print(is_bet(x,y,z))

