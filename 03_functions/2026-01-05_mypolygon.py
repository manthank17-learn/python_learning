import turtle

"""import turtle
bob = turtle.Turtle()
print(bob)
turtle.mainloop()
"""

def square():
    t = turtle.Turtle()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    print(t)
    turtle.mainloop()
square()  