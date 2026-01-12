# typewriter.py
import turtle
from letters import LETTERS

def draw_word(t, word):
    for ch in word.lower():
        if ch in LETTERS:
            LETTERS[ch](t)
        else:
            t.penup()
            t.fd(40)
            t.pendown()

bob = turtle.Turtle()
bob.speed(3)
bob.penup()
bob.goto(-300, 0)
bob.pendown()

draw_word(bob, "manthan")

turtle.mainloop()
