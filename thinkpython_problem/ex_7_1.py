import math

a =  int(input("up to where you waanna get roots for?: "))
def mysqrt(a):
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 0.00000000000001:
            return y
        x = y

import math

def test_square_root():
    print("a  mysqrt(a)        math.sqrt(a)     diff")
    print("-- --------------- ----------------- ----")

    for a in range(1, 10):
        my = mysqrt(a)
        real = math.sqrt(a)
        diff = abs(my - real)
        print(a, my, real, diff)
        
test_square_root()
    
          