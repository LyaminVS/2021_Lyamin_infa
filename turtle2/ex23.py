import turtle
Vx = int(input('Vx '))
Vy = int(input('Vy '))
# Vx = 10
# Vy = 50
ay = float(input('g '))
turtle.shape('turtle')
turtle.speed(0)

x = 0
y = 0
turtle.forward(350)
turtle.left(180)
turtle.forward(700)

turtle.left(180)
turtle.forward(10)
x = -340
y = 0
turtle.speed(1)
for dt in range(0, 800000):
    dt = dt / 10000
    x += Vx*dt
    y += Vy*dt - ay*dt**2/2
    Vy += -ay*dt
    turtle.goto(x, y)
    if (y <= 0 and Vy < 0):
        Vy = -Vy * (2)**(0.5)/2
