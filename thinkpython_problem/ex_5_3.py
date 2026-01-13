
global a , b, c 


a = int(input("enter the first   side of the triangle?:"))
b= int(input("enter the second   side of the triangle?:"))
c= int(input("enter the third   side of the triangle?:"))

def is_triangle(a,b,c):
    if a+b <= c :
        print ("Not possible for a triangle")
    elif b+c <=a :
        print("not possible for a triangle")
    elif a+c <=c:
        print("not possible for a triangle")
    else:
        print("it can be a triangle")

is_triangle(a,b,c)
