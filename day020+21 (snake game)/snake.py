from time import sleep
import turtle
import food

STARTING_POSITIONS = [
    (20, 0),
    (0, 0),
    (-20, 0),
]  # Starting positions of the snake segments


class Snake:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("The 1 and only Snake Game!!")
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)  # Turns off the animation

        self.segments = []
        self.food = food.Food()  # Creates a new instance of the Food class
        self.create_snake()
        self.head = self.segments[0]
        self.score = 0  # Initializes the score to 0
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.color("white")
        self.score_display.penup()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("chartreuse")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def display_score(self):
        self.score_display.goto(0, 260)
        self.score_display.clear()  # Clears the previous score display
        self.score_display.write(
            f"Score: {self.score}", align="center", font=("Arial", 24, "normal")
        )

    def game_over(self):
        self.score_display.goto(0, 0)
        self.score_display.write(
            "GAME OVER", align="center", font=("Arial", 24, "normal")
        )

    def space_to_continue(self):
        self.score_display.goto(0, -30)
        self.score_display.write(
            "Press Space to Continue", align="center", font=("Arial", 16, "normal")
        )
        self.screen.onkey(self.reset_game, "space")
        self.screen.listen()

    def reset_game(self):
        self.score = 0
        self.display_score()
        for segment in self.segments:
            segment.hideturtle()  # Hides the segment
        self.segments.clear()  # Clears the list of segments
        self.create_snake()
        self.food.refresh()
        self.play()  # Restart the game loop

    def play(self):
        game_on = True
        fposition = self.food.refresh()  # Place the food at a random position
        self.display_score()  # Display the initial score
        while game_on:
            for i in range(
                len(self.segments) - 1, 0, -1
            ):  # Moves the segments from the tail to the head
                new_x = self.segments[
                    i - 1
                ].xcor()  # Gets the x coordinate of the segment in front of it
                new_y = self.segments[
                    i - 1
                ].ycor()  # Gets the y coordinate of the segment in front of it
                self.segments[i].goto(
                    new_x, new_y
                )  # Moves the segment to the position of the segment in front of it
            self.segments[0].forward(20)  # Moves the head segment forward by 20 pixels
            self.screen.onkey(
                lambda: (
                    self.segments[0].setheading(90)
                    if self.segments[0].heading() != 270
                    else None
                ),
                "Up",
            )  # Sets the heading of the head segment to up
            self.screen.onkey(
                lambda: (
                    self.segments[0].setheading(270)
                    if self.segments[0].heading() != 90
                    else None
                ),
                "Down",
            )  # Sets the heading of the head segment to down
            self.screen.onkey(
                lambda: (
                    self.segments[0].setheading(180)
                    if self.segments[0].heading() != 0
                    else None
                ),
                "Left",
            )  # Sets the heading of the head segment to left
            self.screen.onkey(
                lambda: (
                    self.segments[0].setheading(0)
                    if self.segments[0].heading() != 180
                    else None
                ),
                "Right",
            )  # Sets the heading of the head segment to right
            self.screen.listen()  # Listens for key presses
            if (
                self.segments[0].xcor() > 280
                or self.segments[0].xcor() < -280
                or self.segments[0].ycor() > 280
                or self.segments[0].ycor() < -280
                or any(
                    self.segments[0].distance(segment) < 10
                    for segment in self.segments[1:]
                )
            ):
                game_on = False  # Ends the game if the head segment goes out of bounds
                self.game_over()  # Displays the game over message
                self.space_to_continue()  # Prompts the player to press space to continue
            if (
                self.segments[0].distance(fposition) < 20
            ):  # Checks if the head segment is close to the food
                fposition = self.food.refresh()  # Refreshes the food position
                self.extend()  # Extends the snake by adding a new segment
                self.score += 1  # Increments the score
                self.display_score()  # Updates the score display

            self.screen.update()  # Updates the screen with the new positions of the segments
            sleep(0.1)

    def exitonclick(self):
        self.screen.exitonclick()  # Exits the game when the user clicks on the screen
