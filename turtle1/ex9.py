import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(0)


def draw(n, prewr):
    a = 50
    r = a * n / 6 / (2 * np.sin(np.pi / n))
    turtle.forward(r - prewr)
    turtle.pendown()
    grad = 180 - 360 / n
    turtle.left(180 - grad / 2)
    for i in range(n):
        turtle.forward(a * n / 6)
        turtle.left(180 - grad)
    turtle.right(180 - grad / 2)
    turtle.penup()
    return r


r = 0
turtle.penup()
for k in range(3, 14):
    r = draw(k, r)
