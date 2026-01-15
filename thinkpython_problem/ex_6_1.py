def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))
"""
the values of the x and y are given 
z= 1+1+1 =3
y = 5 

total = 9 

sqaure = b(3)**2


b(9)

a(9,9)

x=x+1
x=10
and y = 9
b(90)

square= 90**2
8100




"""
