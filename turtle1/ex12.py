import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(1)


def duga(rad):
    for i in range(180):
        turtle.forward(rad * 0.05)
        turtle.right(1)


def circle(rad, direction):
    for i in range(360):
        turtle.forward(rad * 0.05)
        if (direction == 'left'):
            turtle.left(1)
        if (direction == 'right'):
            turtle.right(1)


turtle.penup()
turtle.left(90)
turtle.forward(30 * 0.05 / (2 * np.sin(np.pi / 360)))
turtle.left(90)
turtle.pendown()

turtle.begin_fill()
circle(30, 'left')
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(-40, 50)
turtle.pendown()
turtle.begin_fill()
circle(5, "left")
turtle.color('blue')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(40, 50)
turtle.pendown()
turtle.begin_fill()
circle(5, "left")
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.color('black')
turtle.left(90)
turtle.width(6)
turtle.forward(25)
turtle.penup()
turtle.goto(1 / (2 * np.sin(np.pi / 360)), 5)
turtle.pendown()
turtle.color('red')
duga(20)
