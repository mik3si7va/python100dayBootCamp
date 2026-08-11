from pathlib import Path
from tkinter import Button, Canvas, Label, PhotoImage, Tk

THEME_COLOR = "#375362"

# im givin u full creative control as to how u going to implement this shit just know that a want the following:
# 1. the ui should be called from the brain (quiz_brain) and not from the main.py file
# 2. the ui should display the question and the score and
# 3. the ui should have two buttons (true and false) and when the user clicks on either of them it should call the check_answer method from the brain and pass the answer to it and then the brain should check if the answer is correct or not and then update the score and
# 4. the ui should display a big emoji (🎉) if the answer is correct and a big red cross (❌) if the answer is wrong and then after 1 second it should display the next question and update the score and question number on the ui as well
# 5. no image boundry markers or anything like that just make it look good and simple and clean and minimalistic
# 6. display should be this one: question and popping emojis on the centre; below it the true and false buttons; below that the score (left of the screen) and question number (on the bottom right corner of the screen), these tow in the same line tho ..
# 7. Good luck .. I believe in U !! 😉


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Mythology Quiz")
        self.window.config(padx=40, pady=32, bg=THEME_COLOR)
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(
            width=520,
            height=390,
            bg=THEME_COLOR,
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, columnspan=3, pady=(0, 26))
        self.feedback_text = self.canvas.create_text(
            260,
            92,
            text="",
            font=("Arial", 62, "bold"),
        )
        self.question_text = self.canvas.create_text(
            260,
            230,
            width=470,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 21, "italic"),
            justify="center",
        )

        image_folder = Path(__file__).resolve().parent / "images"
        self.true_image = PhotoImage(file=image_folder / "true.png")
        self.false_image = PhotoImage(file=image_folder / "false.png")

        self.true_button = Button(
            image=self.true_image,
            command=lambda: self.answer("True"),
            borderwidth=0,
            highlightthickness=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            cursor="hand2",
        )
        self.true_button.grid(row=1, column=0, pady=(0, 28))

        self.false_button = Button(
            image=self.false_image,
            command=lambda: self.answer("False"),
            borderwidth=0,
            highlightthickness=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            cursor="hand2",
        )
        self.false_button.grid(row=1, column=2, pady=(0, 28))

        self.score_text = Label(
            self.window,
            text="Score: 0",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 13, "bold"),
        )
        self.score_text.grid(row=2, column=0, sticky="w")

        self.high_score_text = Label(
            self.window,
            text="High Score: 0",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 13, "bold"),
        )
        self.high_score_text.grid(row=2, column=1)

        self.number_text = Label(
            self.window,
            text="Question: 0/0",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 13, "bold"),
        )
        self.number_text.grid(row=2, column=2, sticky="e")

    def display_question(self, question, score, high_score, number, total):
        self.canvas.tag_unbind(self.feedback_text, "<Button-1>")
        self.canvas.config(cursor="")
        self.canvas.itemconfig(self.feedback_text, text="")
        self.canvas.itemconfig(self.question_text, text=question, fill="white")
        self.update_progress(score, high_score, number, total)
        self.set_buttons_enabled(True)

    def answer(self, user_answer):
        self.set_buttons_enabled(False)
        self.quiz.check_answer(user_answer)

    def show_feedback(self, emoji, is_correct):
        color = "#30a46c" if is_correct else "#d64045"
        self.canvas.itemconfig(self.feedback_text, text=emoji, fill=color)
        self.pop_emoji(62)

    def pop_emoji(self, size):
        if size >= 82:
            return
        self.canvas.itemconfig(self.feedback_text, font=("Arial", size, "bold"))
        self.window.after(35, self.pop_emoji, size + 4)

    def update_progress(self, score, high_score, number, total):
        self.score_text.config(text=f"Score: {score}")
        self.high_score_text.config(text=f"High Score: {high_score}")
        self.number_text.config(text=f"Question: {number}/{total}")

    def schedule_next_question(self):
        self.window.after(1000, self.quiz.next_question)

    def show_finished(self):
        self.update_progress(
            self.quiz.score,
            self.quiz.high_score,
            self.quiz.question_number,
            len(self.quiz.question_list),
        )
        self.canvas.itemconfig(self.feedback_text, text="🏆", fill="#d9a400")
        self.canvas.itemconfig(
            self.question_text,
            text=(
                f"Quiz complete!\nFinal score: "
                f"{self.quiz.score}/{self.quiz.question_number}\n\n"
                "Click the trophy to play again"
            ),
        )
        self.canvas.tag_bind(
            self.feedback_text, "<Button-1>", lambda _event: self.quiz.restart()
        )
        self.canvas.config(cursor="hand2")
        self.set_buttons_enabled(False)

    def set_buttons_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def run(self):
        self.window.mainloop()

    def close(self):
        self.quiz.cancelled = True
        self.window.destroy()
