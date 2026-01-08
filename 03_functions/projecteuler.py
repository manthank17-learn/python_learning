import math

def ksqaure():
    global k ,answer1
    k = 322499

    
    answer1 = float(k*(k+1)*(2*k+1))/6
  


def sum_cal():
    global answer2
    answer2 = float(k *(k+1))/2
    

def sumofall():
    solution = answer1*4 + answer2*4 + k+1
    print(solution)

ksqaure()
sum_cal()
sumofall()
