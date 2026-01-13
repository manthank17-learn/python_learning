"""
Docstring for thinkpython_problem.ex_5.4

the problem will have following stack diagram 

main 

recurse(2,3)

recurse(1,5)

recurse(0,6)

result s = 6





"""

def recurse (n,s):
    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)


recurse(-1,0)