import turtle
import random

# basic settings
BACKGROUND_COLOR = "white"
GRID_SIZE = 6
START_X = -250
START_Y = 250
SPACE = 90
COLORS = ["red", "blue", "green", "orange", "purple"]


# returns random position
def random_position(row, col):
    x = START_X + col * SPACE + random.randint(-15, 15)
    y = START_Y - row * SPACE + random.randint(-15, 15)
    return x, y


# draws different random shapes
def draw_shape(pen, size):
    if size > 25:
        for i in range(5):
            pen.forward(size)
            pen.right(72 + random.randint(-10, 10))
    else:
        for i in range(8):
            pen.circle(size / 2)
            pen.right(45 + random.randint(-5, 5))


def main():
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(2)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            x, y = random_position(row, col)
            size = random.randint(15, 40)

            pen.penup()
            pen.goto(x, y)
            pen.pendown()

            pen.color(random.choice(COLORS))
            pen.left(random.randint(0, 360))

            draw_shape(pen, size)

    pen.hideturtle()
    screen.mainloop()


main()
