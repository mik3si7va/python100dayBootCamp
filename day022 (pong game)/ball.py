import turtle


class Ball(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = False
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.25

    def move(self):
        new_x = self.xcor() + self.x_move * self.move_speed
        new_y = self.ycor() + self.y_move * self.move_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.25

    def walling(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce_y()
        elif self.xcor() > 390 or self.xcor() < -390:
            self.bounce_x()
            self.score = True

    def increase_speed(self):
        self.move_speed += 0.1

    def set_speed(self, speed):
        self.move_speed = speed
