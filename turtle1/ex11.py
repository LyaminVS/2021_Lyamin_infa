import turtle

turtle.shape('turtle')
turtle.speed(0)


def circle(rad, direction):
    for i in range(360):
        turtle.forward(rad * 0.05 + 0.5)
        if (direction == 'left'):
            turtle.left(1)
        if (direction == 'right'):
            turtle.right(1)


turtle.left(90)
for i in range(1, 11):
    circle(i, 'left')
    circle(i, 'right')
