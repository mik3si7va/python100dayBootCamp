from os import path
import tkinter as tk

directory = path.dirname(__file__)


class layout:
    def __init__(self, window):
        self.window = window
        self.window.title("Pomodoro Timer")
        self.window.geometry("400x400")
        self.window.resizable(False, False)

    def create_canvas(self):
        canvas = tk.Canvas(self.window, width=400, height=400, highlightthickness=0)
        canvas.place(x=0, y=0)
        return canvas

    def create_background(self, canvas):
        bg = tk.PhotoImage(file=path.join(directory, "pomodoro.png"))
        bg = bg.subsample(3, 3)  # Resize the image to fit the canvas
        canvas.create_image(200, 200, image=bg)
        return bg  # Return the image reference to prevent garbage collection

    def print_title(self, canvas, text="Pomodoro Timer"):
        canvas.delete("title_shadow")  # Clear the canvas before drawing
        canvas.delete("title")  # Clear the canvas before drawing
        canvas.create_text(
            202,
            52,
            text=text,
            fill="black",
            font=("Arial", 24, "bold"),
            tag="title_shadow",
        )
        canvas.create_text(
            200,
            50,
            text=text,
            fill="plum",
            font=("Arial", 24, "bold"),
            tag="title",
        )

    def start_button(self, canvas):
        button = tk.Button(
            self.window,
            text="Start",
            bg="plum",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        button.place(x=150, y=350)
