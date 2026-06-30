from countdown import countDown
import tkinter as tk


class buttons:
    def __init__(self, window):
        self.window = window

    def create_start_button(self, canvas, time=25):
        button = tk.Button(
            self.window,
            text="Start",
            command=lambda: self.start_countdown(
                time, canvas
            ),  # Start a 25-minute countdown
            bg="plum",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        button.place(x=50, y=350)

    def start_countdown(self, time, canvas):
        cd_timer = countDown(time, canvas)  # Set the timer for the specified time
        cd_timer.start()

    def create_reset_button(self, canvas):
        button = tk.Button(
            self.window,
            text="Reset",
            command=lambda: self.reset_countdown(canvas),
            bg="plum",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        button.place(x=300, y=350)

    def reset_countdown(self, canvas):
        # Reset the countdown timer to 25 minutes
        return countDown(25, canvas)
