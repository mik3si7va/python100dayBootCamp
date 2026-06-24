from time import sleep
import turtle
import paddle as pd
import ball as bl
import score as sc

screen = turtle.Screen()
screen.title("THE Pong Game...")


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Turns off the screen updates for smoother animation

paddle_one = pd.Paddle((350, 0))
paddle_two = pd.Paddle((-350, 0))

ball = bl.Ball((0, 0))

scoreboard = sc.Scoreboard()
numMax = 11  # Set the maximum score to end the game

screen.listen()
screen.onkeypress(paddle_one.go_up, "Up")
screen.onkeypress(paddle_one.go_down, "Down")
screen.onkeypress(paddle_two.go_up, "w")
screen.onkeypress(paddle_two.go_down, "s")
screen.onkeypress(lambda: ball.set_speed(ball.move_speed + 0.05), "space")
screen.onkeypress(lambda: ball.set_speed(ball.move_speed - 0.05), "Escape")

print("Press 'Space' to increase ball speed and 'Escape' to decrease ball speed.")
print(
    "Use 'Up' and 'Down' arrows for Player 1 and 'W' and 'S' keys for Player 2 to move the paddles."
)
print(f"The game will end when one player reaches a score of {numMax}.")

game_on = True
while game_on:
    sleep(0.01)  # Controls the speed of the ball
    screen.update()  # Updates the screen with the latest changes
    ball.move()
    ball.walling()
    # Check for collision with paddles
    if ball.distance(paddle_one) < 60 and ball.xcor() > 330:
        ball.bounce_x()
        ball.increase_speed()  # Increase speed on paddle hit
    if ball.distance(paddle_two) < 60 and ball.xcor() < -330:
        ball.bounce_x()
        ball.increase_speed()  # Increase speed on paddle hit

    # Check for scoring
    if ball.score:
        if ball.xcor() > 390:
            scoreboard.increase_score_one()
        elif ball.xcor() < -390:
            scoreboard.increase_score_two()
        ball.reset_position()
        ball.score = False
    if scoreboard.score_one >= numMax or scoreboard.score_two >= numMax:
        game_on = False
        winner = "Player 1" if scoreboard.score_one >= numMax else "Player 2"
        print(f"{winner} wins the game!")
        scoreboard.print_winner(winner)

print("Game Over! Thanks for playing.")
screen.exitonclick()  # Waits for a mouse click to exit the game
