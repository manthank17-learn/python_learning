# letters.py
import turtle


# Helper primitives


LETTER_HEIGHT = 60
LETTER_WIDTH = 40
SPACING = 20

def begin_letter(t):
    """Save turtle state at letter start"""
    return t.heading(), t.ycor()

def end_letter(t, start_heading, start_y):
    """Restore alignment and move to next letter"""
    t.penup()
    t.setheading(start_heading)
    t.sety(start_y)
    t.fd(LETTER_WIDTH + SPACING)
    t.pendown()


# Letter definitions


def draw_a(t):
    h, y = begin_letter(t)

    t.lt(60)
    t.fd(LETTER_HEIGHT)
    t.rt(120)
    t.fd(LETTER_HEIGHT)
    t.bk(LETTER_HEIGHT / 2)
    t.rt(120)
    t.fd(LETTER_HEIGHT / 2)

    end_letter(t, h, y)

def draw_m(t):
    h, y = begin_letter(t)

    t.lt(90)
    t.fd(LETTER_HEIGHT)
    t.rt(150)
    t.fd(LETTER_HEIGHT / 1.5)
    t.lt(120)
    t.fd(LETTER_HEIGHT / 1.5)
    t.rt(150)
    t.fd(LETTER_HEIGHT)

    end_letter(t, h, y)

def draw_n(t):
    h, y = begin_letter(t)

    t.lt(90)
    t.fd(LETTER_HEIGHT)
    t.rt(150)
    t.fd(LETTER_HEIGHT * 1.1)
    t.lt(150)
    t.fd(LETTER_HEIGHT)

    end_letter(t, h, y)

def draw_t(t):
    h, y = begin_letter(t)

    t.lt(90)
    t.fd(LETTER_HEIGHT)
    t.bk(LETTER_HEIGHT / 2)
    t.rt(90)
    t.bk(LETTER_WIDTH / 2)
    t.fd(LETTER_WIDTH)

    end_letter(t, h, y)

def draw_h(t):
    h, y = begin_letter(t)

    t.lt(90)
    t.fd(LETTER_HEIGHT)
    t.bk(LETTER_HEIGHT / 2)
    t.rt(90)
    t.fd(LETTER_WIDTH / 2)
    t.lt(90)
    t.fd(LETTER_HEIGHT / 2)
    t.bk(LETTER_HEIGHT)

    end_letter(t, h, y)



# Dispatch table


LETTERS = {
    'a': draw_a,
    'm': draw_m,
    'n': draw_n,
    't': draw_t,
    'h': draw_h,
}
