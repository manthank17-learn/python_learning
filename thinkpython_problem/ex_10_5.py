
"""
ex 10.5 is_sorted(t)

"""
t =[1,2,3,4]
j= [2,1,3,4]

def is_sorted(t):
    for i in range (len(t) -1):
        if t[i] > t[i + 1]:
            return False
    return True    

print(is_sorted(t))        
print(is_sorted(j))
           
