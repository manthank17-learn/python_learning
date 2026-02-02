"""

chapter 10 lists

"""

t = ["a","c","f","b","f","g","r","y","g","f"]


T = [1,22,33,44,55,66,77,88,99]
def add_all(T):
    global total
    total = 0
    for x in T:
        total +=x
    return total

print(add_all(T))


print(sum(T))

def cap_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res 
print(cap_all(t))