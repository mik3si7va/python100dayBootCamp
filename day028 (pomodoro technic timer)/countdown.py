import tkinter as tk

import time


class countDown:
    def __init__(self, minutes, canvas):
        self.minutes = minutes
        self.seconds = 0
        self.canvas = canvas

    def start(self):
        while self.minutes > 0 or self.seconds > 0:
            self.canvas.delete("timer_shadow")  # Clear the canvas before drawing
            self.canvas.delete("timer")  # Clear the canvas before drawing
            self.draw(self.canvas)
            self.canvas.update()
            if self.seconds == 0:
                if self.minutes > 0:
                    self.minutes -= 1
                    self.seconds = 59
                else:
                    break
            else:
                self.seconds -= 1
            time.sleep(1)
        print("Time's up!")

    def draw(self, canvas):

        canvas.create_text(
            202,
            272,
            text=f"{self.minutes:02d}:{self.seconds:02d}",
            fill="black",
            font=("Arial", 48, "bold"),
            tag="timer_shadow",
        )

        canvas.create_text(
            200,
            270,
            text=f"{self.minutes:02d}:{self.seconds:02d}",
            fill="plum",
            font=("Arial", 48, "bold"),
            tag="timer",
        )
