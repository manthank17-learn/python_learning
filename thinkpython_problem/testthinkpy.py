import turtle
import math

def pie(t, r, n):
    """Draw n radii from center, evenly spaced"""
    angle = 360 / n
    for i in range(n):
        t.fd(r)
        t.bk(r)
        t.lt(angle)

def polygon_at_radius(t, r, n):
    """Draw n-sided polygon with vertices at distance r from center"""
    angle = 360 / n
    chord = 2 * r * math.sin(math.radians(angle / 2))
    
    # Move to first vertex
    t.penup()
    t.fd(r)
    t.pendown()
    
    # Adjust heading to draw along perimeter
    t.lt(90 + angle / 2)
    
    # Draw polygon
    for i in range(n):
        t.fd(chord)
        t.lt(angle)

def draw_shape(t, radius, num_sides):
    """Draw pie + polygon for any number of sides"""
    pie(t, radius, num_sides)
    
    # Reset to center
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    
    polygon_at_radius(t, radius, num_sides)

# Main
bob = turtle.Turtle()
bob.speed(0)

# Change these two parameters to draw any shape
draw_shape(bob, radius=100, num_sides=2000)

turtle.mainloop()