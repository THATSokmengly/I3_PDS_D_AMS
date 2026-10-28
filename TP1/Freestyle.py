
import turtle
import math
import colorsys

# Create the turtle and screen
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.setup(800, 800)
s.title("Colorful Turtle Art")

# Turtle settings
t.speed(0)
t.width(2)
t.hideturtle()

# Draw the colorful pattern
for i in range(360):
    h = (0.85 + i / 720) % 1.0
    c = colorsys.hsv_to_rgb(h, 0.9, 1)

    t.pencolor(c)

    r = 220 * math.sin(math.radians(i))
    x = r * math.cos(math.radians(i))
    y = r * math.sin(math.radians(i))

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)

# Keep the window open
turtle.done()

