import copy

from turtleInstance import TurtleInstance as TI
import turtle

colors = ["red", "blue", "green", "yellow", "purple"]

screen = turtle.Screen()
screen.setup(width=900, height=400)
screen.bgcolor("darkgray")

race_finish = 300
race_start = -400


def draw_finish_line(where):
    finish_line = turtle.Turtle(visible=False)
    finish_line.color("black")
    finish_line.speed("fastest")
    finish_line.penup()
    finish_line.goto(where, -150)
    finish_line.pendown()
    finish_line.pensize(7)
    finish_line.left(90)
    finish_line.forward(300)


draw_finish_line(race_finish)
draw_finish_line(race_start)

tim = TI(colors[0], (race_start, -100))
toby = TI(colors[1], (race_start, -50))
marta = TI(colors[2], (race_start, 0))
mike = TI(colors[3], (race_start, 50))
jonas = TI(colors[4], (race_start, 100))


def clear():
    for turtle in [tim, toby, marta, mike, jonas]:
        turtle.tim.clear()
        turtle.tim.penup()
        turtle.tim.setpos(race_start, turtle.pos[1])
        turtle.tim.pendown()


def draw_winner_big(turtle):
    turtle.tim.clear()
    turtle.tim.penup()
    turtle.tim.setpos(-20, -50)
    turtle.tim.pendown()
    turtle.tim.write(
        f"{turtle.tim.color()[0].capitalize()} wins!",
        align="center",
        font=("Arial", 30, "bold"),
    )
    turtle.tim.penup()
    turtle.tim.shapesize(2, 2, 2)
    turtle.tim.setpos(race_finish + 30, turtle.pos[1])
    turtle.tim.pendown()


def start_race():
    while (
        tim.tim.xcor() < race_finish
        and toby.tim.xcor() < race_finish
        and marta.tim.xcor() < race_finish
        and mike.tim.xcor() < race_finish
        and jonas.tim.xcor() < race_finish
    ):
        tim.random_move()
        toby.random_move()
        marta.random_move()
        mike.random_move()
        jonas.random_move()
        for turtle in [tim, toby, marta, mike, jonas]:
            if turtle.tim.xcor() >= race_finish:
                draw_winner_big(turtle)
                return


screen.onkey(lambda: start_race(), "space")
screen.listen()

screen.exitonclick()
