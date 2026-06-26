from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.color(self.random_color())
        new_car.goto(300, self.random_y_position())
        self.all_cars.append(new_car)
        return new_car

    def detect_collision(self, player):
        for car in self.all_cars:
            if (
                abs(car.xcor() - player.xcor()) < 30
                and abs(car.ycor() - player.ycor()) < 20
            ):
                return True
        return False

    def random_color(self):
        import random

        return random.choice(COLORS)

    def random_y_position(self):
        import random

        return random.randrange(-250, 250, 50)

    def move(self, car):
        car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
