import math 
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

   #   print(factorial(20))


def estimate_pi():
    constant = 2 * math.sqrt(2) / 9801
    total = 0
    k = 0

    while True:
        term = (factorial(4*k) * (1103 + 26390*k)) / ((factorial(k)**4) * (396**(4*k)))
        total += term

        estimate = 1 / (constant * total)

        if abs(estimate - math.pi) < 1e-15:
            return estimate

        k += 1
print(estimate_pi())