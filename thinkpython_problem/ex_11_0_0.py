d = {}
d["a"] = 5
d["b"] = 3
d["a"]+= 10
print(d)
print(d["a"])

def hist(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] =1
        else:
            d[c]+=1
    return d
def print_hist(h):
    for c in h:
        print(c,h[c])
h = hist('banana')
print_hist(h)

def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k 
    raise LookupError()    

h = hist('parrot')
k = reverse_lookup(h,1)
print(k)