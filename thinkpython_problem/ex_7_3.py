# Srinivasa Ramanujan loop for math.pi
"""
Docstring for thinkpython_problem.ex_7_3
1. have a while loop that put the value of k and i and run it until math.pi - mypi =1e-15
2.

"""
import math
def factorial(n):
     if n ==0:
          return 1
     else:
          return n * factorial(n-1)



def estimate_pi():
    constant = 2* math.sqrt(2)/9801
    k = 0
    while True:
         mypie  = constant *((factorial(4*k) * ( 1103 + 26390 *k))/ ((factorial(k))**4) * (396)**(4*(k)))
         if abs((math.pi)-(1/mypie)) < 0.0000000000000001:
            return (1/mypie)

print(estimate_pi())
     
        