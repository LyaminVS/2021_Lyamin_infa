import turtle

inp = list(input())

turtle.shape('turtle')
turtle.speed(0)
n = 0
f = open('/Users/vasilij/pylabs/pythonProject/nums')
numbers = [line for line in f]
f.close()
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
for j in range(len(numbers)):
    numbers[j] = numbers[j].split(',')
    for k in range(len(numbers[j])):
        numbers[j][k] = float(numbers[j][k])
for i in inp:
    n = 0
    for elem in numbers[int(i)]:
        if (elem == -1):
            turtle.penup()
            n -= 1
        elif (elem == -2):
            turtle.pendown()
            n -= 1
        elif (n % 2 == 0):
            if (elem == -3):
                turtle.forward(2 * 10 * 2 ** (0.5))
            else:
                turtle.forward(2 * elem)
        else:
            turtle.right(elem)
        n += 1
    turtle.penup()
    turtle.forward(2 * 20)
    turtle.pendown()
