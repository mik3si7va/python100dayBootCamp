import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
step = 0
while game_is_on:
    time.sleep(0.1)
    for car in car_manager.all_cars:
        if -32 < car.xcor() < 32 and car_manager.detect_collision(player):
            game_is_on = False
            scoreboard.game_over()

    for car in car_manager.all_cars:
        if car.xcor() < -320:
            car.hideturtle()
            car_manager.all_cars.remove(car)
    if (random.random() < 0.8) and step % 13 == 0:
        for _ in range(random.randint(3, 7)):
            car_manager.create_car()
    for car in car_manager.all_cars:
        car_manager.move(car)
    screen.update()
    if player.ycor() > 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()
    step += 1

screen.exitonclick()
