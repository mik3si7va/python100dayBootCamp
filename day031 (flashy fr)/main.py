import tkinter as tk
import pandas as pd
import random
import time
from os import path

BACKGROUND_COLOR = "#B1DDC6"
BACK_COLOR = "#91c2af"

directory = path.dirname(__file__)
data_file = path.join(directory, "data/french_words.csv")
known_words_file = path.join(directory, "data/known_words.csv")
words = {}
with open(data_file, "r", encoding="utf-8") as file:
    data = pd.read_csv(file)
    words = data.to_dict(orient="records")

if path.exists(known_words_file):
    known_words = pd.read_csv(known_words_file).to_dict(orient="records")
else:
    known_words = []

known_french_words = [word["French"] for word in known_words]
words = [word for word in words if word["French"] not in known_french_words]

current_card = {}
scoreboard = len(known_words)
playing = True


def save_known_word():
    known_words.append(current_card)
    pd.DataFrame(known_words).to_csv(known_words_file, index=False)


def next_card():
    global current_card
    global playing
    if playing:
        if len(words) == 0:
            card.config(file=path.join(directory, "images/card_front.png"))
            lang_label.config(text="Done", fg="black", bg="white")
            word_label.config(text="No more words", fg="black", bg="white")
            score_label.config(text=scoreboard)
            return

        current_card = random.choice(words)
        card.config(file=path.join(directory, "images/card_front.png"))
        lang_label.config(text="French", fg="black", bg="white")
        word_label.config(text=current_card["French"], fg="black", bg="white")
        score_label.config(text=scoreboard)

        window.update()
        time.sleep(3)
        card.config(file=path.join(directory, "images/card_back.png"))
        lang_label.config(text="English", fg="white", bg=BACK_COLOR)
        word_label.config(text=current_card["English"], fg="white", bg=BACK_COLOR)
        playing = False


def score():
    global playing
    global scoreboard
    if not playing:
        playing = True
        words.remove(current_card)
        save_known_word()
        scoreboard += 1
        next_card()


def fail():
    global playing
    if not playing:
        playing = True
        next_card()


# print(words)

window = tk.Tk()
window.title("Flashy French")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card = tk.PhotoImage(file=path.join(directory, "images/card_front.png"))

right = tk.PhotoImage(file=path.join(directory, "images/right.png"))
wrong = tk.PhotoImage(file=path.join(directory, "images/wrong.png"))

btn_right = tk.Button(image=right, highlightthickness=0, command=score)
btn_right.grid(row=1, column=1)

btn_wrong = tk.Button(image=wrong, highlightthickness=0, command=fail)
btn_wrong.grid(row=1, column=0)

lang_label = tk.Label(
    text="",
    font=("Arial", 40, "italic"),
    fg="black",
    highlightthickness=0,
    bg="white",
)
lang_label.place(x=400, y=150, anchor="center")

word_label = tk.Label(
    text="",
    font=("Arial", 60, "bold"),
    fg="black",
    highlightthickness=0,
    bg="white",
)
word_label.place(x=400, y=263, anchor="center")

score_label = tk.Label(
    text="0",
    font=("Arial", 60, "bold"),
    fg="black",
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
)
score_label.place(x=400, y=590, anchor="center")

canvas.create_image(400, 263, image=card)
canvas.grid(row=0, column=0, columnspan=2)

next_card()

window.mainloop()
