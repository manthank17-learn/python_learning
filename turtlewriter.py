import math,turtle

def draw_a(t):
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)

    t.penup()
    t.goto(0,0)
    t.pendown()



    t.setheading(0)

    t.lt(120)
    t.fd(60)
    t.lt(60)
    t.fd(40)

def draw_m(t):
    t.lt(90)
    t.fd(100)
    
    t.lt(140)
    
    t.fd(60)

    t.rt(90)
    t.fd(60)
    t.setheading(270)
    t.fd(100)
    
    
bob = turtle.Turtle()
draw_m(bob)
turtle.mainloop()