import turtle
import random


class TurtleInstance:
    def __init__(self, color, pos, shape="turtle"):
        self.tim = turtle.Turtle(visible=False)
        self.pos = pos
        self.screen = turtle.Screen()
        turtle.colormode(255)
        self.tim.color(color)
        self.tim.shape(shape)
        self.tim.speed("fastest")
        self.tim.penup()
        self.tim.setpos(pos)
        self.tim.showturtle()

    def move(self, distance):
        self.tim.forward(distance)

    def random_move(self, min_distance=1, max_distance=10):
        distance = random.randint(min_distance, max_distance)
        self.move(distance)
