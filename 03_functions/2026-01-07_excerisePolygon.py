import turtle
import math

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


def circle(t, r):
    n = 50                      # number of sides (more = smoother)
    circumference = 2 * math.pi * r
    length = circumference / n
    polygon(t, n, length)

def arc(t,r,angle):
    n = 100
    circumference = 2 * math.pi * r
    lenght = circumference /n

    steps =int ( n* angle /360)

    for i in range(steps):
        t.fd(lenght)
        t.lt(360/n)

       



bob = turtle.Turtle()
#arc(bob,100,100)
arc(bob,100,90)
#arc(bob,100,360)

turtle.mainloop()