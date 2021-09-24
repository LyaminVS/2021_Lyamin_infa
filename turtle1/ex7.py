import turtle

turtle.shape('turtle')
turtle.speed(0)
f = 1
for i in range(72 * 10):
    f += 0.01
    turtle.forward(f)
    turtle.left(5)
