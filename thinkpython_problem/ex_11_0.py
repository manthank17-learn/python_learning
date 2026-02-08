#this chapter is about dict()

eng2sp = dict()

eng2sp['one'] = 'uno'

print(eng2sp)

eng2sp = {'one':'uno','two':'dos','three':'tres'}
print(eng2sp)

print('one' in eng2sp)

print('uno' in eng2sp)

vals = eng2sp.values()
print('uno' in vals)


def hist(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] =1
        else:
            d[c]+=1
    return d

h = hist('brontosaurus')
print(h)  

def print_hist(h):
    for c in h:
        print(c,h[c])

print_hist(h)

print("-"*4)
h = hist('manthan')
print_hist(h)