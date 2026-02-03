"""
cumsum creates a new list that is [1....,i]
but each i postion get total upto that place
"""
t = [1,2,3,4,5,61,23,44,55]

def cumsum(t):
    total = 0
    res = []
    for x in t:
        
        total= total +x
        res.append(total)
    return res

print(cumsum(t))    
        
