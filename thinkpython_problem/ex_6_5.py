a=int(input("enter a: "))
b=int(input("enter b: "))

def gcd(a,b):
    if b==0:
        return a
    else:
        r = a%b
        return gcd(b,r)
    
print(gcd(a,b))