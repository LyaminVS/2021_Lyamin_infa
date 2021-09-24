import turtle

turtle.shape('turtle')
turtle.speed(0)


def circle():
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)


for j in range(6):
    turtle.left(360 / 6)
    circle()
