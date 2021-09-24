import turtle

turtle.shape('turtle')
for i in range(1, 11):
    for k in range(4):
        turtle.forward(i * 10)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
