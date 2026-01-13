import turtle

def koch(t, length, n):
    if n == 0:
        t.fd(length)
        return
    koch(t, length / 3, n - 1)
    t.lt(60)
    koch(t, length / 3, n - 1)
    t.rt(120)
    koch(t, length / 3, n - 1)
    t.lt(60)
    koch(t, length / 3, n - 1)

def snowflake(t, length, n):
    for _ in range(3):
        koch(t, length, n)
        t.rt(120)

bob = turtle.Turtle()
bob.speed(0)

snowflake(bob, 300, 4)

turtle.mainloop()
