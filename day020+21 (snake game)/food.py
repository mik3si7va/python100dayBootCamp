import random
import turtle


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.shape("turtle")  # Sets the shape of the food to a turtle
        self.color("red")  # Sets the color of the food to red
        self.penup()  # Lifts the pen up so it doesn't draw when moving
        self.speed("fastest")  # Sets the speed of the food to fastest

    def refresh(self):
        x = random.randint(
            -280, 280
        )  # Generates a random x-coordinate within the screen bounds
        y = random.randint(
            -280, 280
        )  # Generates a random y-coordinate within the screen bounds
        self.goto(x, y)  # Moves the food to the new random position
        return (x, y)  # Returns the new position of the food as a tuple
