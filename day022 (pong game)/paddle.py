import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:  # Prevent paddle from going off the top of the screen
            y = self.ycor()
            y += 20
            self.sety(y)

    def go_down(self):
        if self.ycor() > -250:  # Prevent paddle from going off the bottom of the screen
            y = self.ycor()
            y -= 20
            self.sety(y)
