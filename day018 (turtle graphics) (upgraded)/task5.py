import turtle

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


timmy = turtle.Turtle()
timmy.color("chartreuse")
timmy.pensize(2)
timmy.speed(77)
# i = 0
# while True:
#     # for i in range(52):
#     color = rainbow_colors[i % len(rainbow_colors)]
#     timmy.color(color)
#     timmy.circle(77)
#     timmy.left(7)
#     i += 1


def draw_spirograph(size_of_gap, diameter):
    for k in range(int(360 / size_of_gap)):
        timmy.color(rainbow_colors[k % len(rainbow_colors)])
        timmy.circle(diameter)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5, 121)

screen = turtle.Screen()
screen.exitonclick()
