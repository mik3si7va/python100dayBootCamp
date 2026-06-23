import turtle
import random

tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)


def clear():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.pendown()


screen.listen()
screen.onkey(lambda: tim.forward(10), "Up")
screen.onkey(lambda: tim.backward(10), "Down")
screen.onkey(lambda: tim.left(10), "Left")
screen.onkey(lambda: tim.right(10), "Right")
screen.onkey(clear, "c")

screen.exitonclick()
