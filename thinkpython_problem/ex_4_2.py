"""
Docstring for thinkpython_problem.ex_4_1

Think Python – Exercise 4.1
Draw flowers using turtle graphics.
Uses arc → petal → flower abstraction.


"""
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
    n = n = int(100 * angle / 360) + 1

    circumference = 2 * math.pi * r
    lenght = circumference /n

    #steps =int ( n* angle /360)

    for i in range(n):
        t.fd(lenght)
        t.lt(angle/n)


def petal(t, r, angle):
    arc(t, r, angle)
    t.lt(180 - angle)
    arc(t, r, angle)
    t.lt(180 - angle)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)

bob = turtle.Turtle()
flower(bob, n=30, r=50, angle=20)



turtle.mainloop()



