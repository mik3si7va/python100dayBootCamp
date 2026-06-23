import random
from turtle import Turtle, Screen, getshapes

rainbow_names = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]


def draw_broken_shape(angle, num_sides):
    for _ in range(num_sides):
        for _ in range(10):
            timmy.forward(5)
            timmy.up()
            timmy.forward(5)
            timmy.down()
        timmy.right(angle)


timmy = Turtle()


timmy.shape("classic")
timmy.color("blue", "chartreuse")


for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.up()
timmy.goto(-100, -100)
timmy.down()


draw_broken_shape(90, 4)


timmy.up()
timmy.goto(-300, 300)
timmy.down()

for i in range(3, 11):
    angle = 360 / i
    timmy.color((rainbow_names[(i - 3) % len(rainbow_names)]).lower())
    draw_broken_shape(angle, i)

screen = Screen()
screen.exitonclick()
