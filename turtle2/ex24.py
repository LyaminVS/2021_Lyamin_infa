from random import randint
import turtle

time = int(input("Время: "))
number = int(input("Количество черепах: "))
size = float(input("Размер: "))
gas = bool(int(input("Реальность газа: ")))
const = int(input("Сила отталкивания (притяжения): "))


class Particle:

    def __init__(self, turtle, x=0, y=0, speedx=50, speedy=50):
        self.turtle = turtle
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.turtle.penup()
        self.turtle.shapesize(size)
        self.turtle.speed(0)

    def move(self):
        self.x += self.speedx * 0.01
        self.y += self.speedy * 0.01
        self.turtle.goto(self.x, self.y)
        if abs(self.x) >= 200 and self.x * self.speedx > 0:
            self.xreverse()
        if abs(self.y) >= 200 and self.y * self.speedy > 0:
            self.yreverse()

    def xreverse(self):
        self.speedx *= (-1)

    def yreverse(self):
        self.speedy *= (-1)

    def dmove(self, part2):

        dx = part2.x - self.x
        dy = part2.y - self.y
        self.speedx -= dx * const / (dx ** 2 + dy ** 2) ** 1.5
        self.speedy -= dy * const / (dx ** 2 + dy ** 2) ** 1.5


particles = []

turtle.shapesize(0.000000001)
turtle.width(10)
turtle.penup()
turtle.goto(205.1, 205.1)
turtle.pendown()
turtle.goto(205.1, -205.1)
turtle.goto(-205.1, -205.1)
turtle.goto(-205.1, 205.1)
turtle.goto(205.1, 205.1)

for i in range(number):
    particles.append(Particle(turtle.Turtle(shape='circle'), randint(-199, 199), randint(-199, 199), randint(-50, 50),
                              randint(-50, 50)))

for k in range(time):
    if gas:
        for part1 in particles:
            for part2 in particles:
                if part1 != part2:
                    part1.dmove(part2)
    for particle in particles:
        particle.move()
