import turtle
import numpy as np

n = int(input())
turtle.shape('turtle')
turtle.speed(n / 10)
turtle.left(180)
for i in range(n):
    turtle.forward(200)
    turtle.left(180 - 180 / n)
