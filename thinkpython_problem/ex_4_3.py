import turtle
import math




def pie(t, n,length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.bk(length)
        t.lt(angle)

def polygon(t,n,lenght):
    angle = 180 -((( n-2)*(180))/ (2*n))
    t.fd(lenght)
    t.lt(angle)
    #angle = 360 /n 
    #t.lt(180-angle*2)
    for i in range(n):
        t.fd(lenght) 
        t.lt(angle)

"""def polygon(t, n, radius):
    angle = 360 / n
    t.fd(radius)
    t.lt(180 - angle / 2)

    side = 2 * radius * math.sin(math.pi / n)

    for i in range(n):
        t.fd(side)
        t.lt(angle)
"""
bob = turtle.Turtle()

pie(bob, 5, 100)
polygon(bob, 5, 100)

turtle.mainloop()
