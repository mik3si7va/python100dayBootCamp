import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_one = 0
        self.score_two = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 220)
        self.write(
            f"{self.score_one} :: {self.score_two}",
            align="center",
            font=("Arial", 24, "bold"),
        )
        self.goto(0, 260)
        self.write(
            "SCOREBOARD",
            align="center",
            font=("Arial", 18, "bold"),
        )

    def print_winner(self, winner):
        self.goto(0, 0)
        self.write(
            f"{winner} wins the game!",
            align="center",
            font=("Arial", 24, "bold"),
        )

    def increase_score_one(self):
        self.score_one += 1
        self.update_scoreboard()

    def increase_score_two(self):
        self.score_two += 1
        self.update_scoreboard()
