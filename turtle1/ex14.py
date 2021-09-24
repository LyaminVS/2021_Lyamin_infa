import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)


def duga(rad):
    for i in range(180):
        turtle.forward(rad * 0.05)
        turtle.right(1)


for j in range(10):
    duga(20)
    duga(4)
