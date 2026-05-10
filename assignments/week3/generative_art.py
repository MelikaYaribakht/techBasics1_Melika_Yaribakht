import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

colors = ["red", "blue", "green", "orange", "purple"]

for row in range(6):
    for col in range(6):

        x = -250 + col * 90 + random.randint(-15, 15)
        y = 250 - row * 90 + random.randint(-15, 15)

        pen.penup()
        pen.goto(x, y)
        pen.pendown()

        pen.color(random.choice(colors))

        size = random.randint(15, 40)

        pen.left(random.randint(0, 360))

        if size > 25:

            for i in range(5):
                pen.forward(size)
                pen.right(72 + random.randint(-10, 10))

        else:

            for i in range(8):
                pen.circle(size / 2)
                pen.right(45 + random.randint(-5, 5))

pen.hideturtle()
screen.mainloop()
