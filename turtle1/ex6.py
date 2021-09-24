import turtle

n = int(input())
turtle.shape('turtle')
turtle.speed(0)
grad = 180 - (360 / n)
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(grad)
