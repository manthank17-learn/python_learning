import turtle

"""
this is koch curve
"""
def koch(t, length, n):
    if n == 0:
        t.fd(length)
    else:
        koch(t, length/3, n-1)
        t.lt(60)
        koch(t, length/3, n-1)
        t.rt(120)
        koch(t, length/3, n-1)
        t.lt(60)
        koch(t, length/3, n-1)

def snowflake(t):
    
    koch(t ,300, 4)
    t.setheading(240)
    koch(t ,300, 4)
    t.setheading(120)
    koch(t,300,4)

bob = turtle.Turtle()
bob.speed(0)

snowflake(bob)



turtle.mainloop()
