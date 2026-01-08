import turtle 
def sqaure(t,lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

bob = turtle.Turtle()
sqaure(bob,1000)

turtle.mainloop()