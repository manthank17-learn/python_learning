import math

def mysqrt(a): #newtons formula for finding sqrt with just assumptions 
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 0.0000001:
            return y
        x = y


def test_square_root():#this what i was struggling with but i had the idea of using f string to attain the prefect formating 
    print(f"{'a':>2} {'mysqrt(a)':>14} {'math.sqrt(a)':>14} {'diff':>12}")
    print(f"{'-'*2} {'-'*14} {'-'*14} {'-'*12}")

    for a in range(1,10):
        my = mysqrt(a)
        real = math.sqrt(a)
        diff = abs(my - real)

        print(f"{a:2d} {my:14.10f} {real:14.10f} {diff:12.2e}")


test_square_root()
