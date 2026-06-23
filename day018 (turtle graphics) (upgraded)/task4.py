import random
import turtle

rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim = turtle.Turtle()
tim.shape("classic")
tim.pensize(5)
tim.speed("fastest")

angles = [0, 90, 180, 270]

turtle.colormode(255)

while True:
    angle = random.choice(angles)
    tim.color(random_color())
    tim.forward(7)
    tim.right(angle)
