from logging import root
import tkinter as tk
from os import path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#edf7dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PACE = 1000  # 1 second in milliseconds

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

reset = False  # Global variable to track reset state
break_count = 0  # Global variable to track the number of breaks taken
break_time = False  # Global variable to track if it's break time
long_break = False  # Global variable to track if it's long break time
stop = False  # Global variable to track if the timer is stopped
started = False  # Global variable to track if the timer has started


# function to update the timer display
def update_timer_display(minutes, seconds):
    canvas.itemconfig("timer", text=f"{minutes:02d}:{seconds:02d}")
    canvas.itemconfig("timer_shadow", text=f"{minutes:02d}:{seconds:02d}")


def update_title_display(title):
    canvas.itemconfig("title", text=title)
    canvas.itemconfig("title_shadow", text=title)


def countdown(count):
    minutes = count // 60
    seconds = count % 60
    global reset
    global long_break
    global break_time
    global break_count
    global stop
    if stop:
        update_timer_display(0, 0)
        update_title_display("TIMER")
        canvas.itemconfig("checks", text="")
        return  # Exit the function if the timer is stopped
    if not reset and not stop:
        update_timer_display(minutes, seconds)
        if count > 0 and not stop:
            window.after(PACE, countdown, count - 1)  # Start with 25:00
        elif count == 0 and not stop:
            # make the program ring a bell sound when the countdown reaches 0
            # costimeze the bell sound to your liking
            window.bell()  # Ring the bell sound!!
            if long_break:
                break_time = False
                long_break = False
                reset_timer()  # Reset the timer after break
                update_title_display("WORK")
                start_timer(WORK_MIN)  # Start work session after long break

            if break_time:
                break_time = False
                update_title_display("WORK")
                start_timer(WORK_MIN)  # Start work session after break
            else:

                break_count += 1
                break_time = True
                update_title_display("BREAK")
                # When the countdown reaches 0, update the checks label
                current_checks = canvas.itemcget("checks", "text")
                canvas.itemconfig("checks", text=current_checks + "✔")
                if break_count % 4 == 0:
                    long_break = True
                    start_timer(
                        LONG_BREAK_MIN
                    )  # Start long break after 4 work sessions
                else:
                    start_timer(SHORT_BREAK_MIN)  # Start short break after work session


def reset_timer():
    global reset
    global break_count
    global break_time
    global long_break
    global stop
    global started
    started = False
    reset = True
    break_count = 0
    break_time = False
    long_break = False
    stop = True
    update_timer_display(0, 0)
    update_title_display("TIMER")
    canvas.itemconfig("checks", text="")


def start_timer(mins=WORK_MIN):
    global reset
    reset = False
    update_title_display("WORK" if not break_time else "BREAK")
    if long_break:
        update_title_display("LONG BREAK")
    countdown(mins * 60)  # Start with 25:00


def restart_timer(mins=WORK_MIN):
    global stop
    reset_timer()  # Reset the timer before restarting
    stop = False
    start_timer(mins)  # Restart the timer with work session


def fork_timer():
    global stop
    global started
    if stop:
        restart_timer(WORK_MIN)  # Restart the timer with work session
    elif not started:
        started = True
        start_timer(WORK_MIN)  # Start the timer with work session


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(width=400, height=400)
canvas = tk.Canvas(width=400, height=400, highlightthickness=0)
img = tk.PhotoImage(file=path.join(path.dirname(__file__), "pomodoro.png"))
img = img.subsample(3, 3)  # Resize the image to fit the canvas
canvas.create_image(200, 200, image=img)
canvas.create_text(
    202, 82, text="TIMER", fill=RED, font=(FONT_NAME, 35, "bold"), tags="title_shadow"
)
canvas.create_text(
    200, 80, text="TIMER", fill=YELLOW, font=(FONT_NAME, 35, "bold"), tags="title"
)
canvas.create_text(
    202, 272, text="00:00", fill=RED, font=(FONT_NAME, 35, "bold"), tags="timer_shadow"
)
canvas.create_text(
    200, 270, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"), tags="timer"
)

start_button = tk.Button(
    text="Start",
    highlightthickness=0,
    bg=RED,
    fg=YELLOW,
    relief="flat",
    command=fork_timer,
    bd=3,
)
start_button.place(x=40, y=350)
reset_button = tk.Button(
    text="Reset",
    highlightthickness=0,
    bg=RED,
    fg=YELLOW,
    relief="flat",
    command=reset_timer,
    bd=3,
)
reset_button.place(x=320, y=350)

checks_label = canvas.create_text(
    200, 370, text="", fill=GREEN, font=(FONT_NAME, 20, "bold"), tags="checks"
)

canvas.place(x=0, y=0)

window.mainloop()
