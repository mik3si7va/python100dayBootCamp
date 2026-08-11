from ui import QuizInterface


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.high_score = 0
        self.question_list = q_list
        self.current_question = None
        self.cancelled = False
        # Add the UI class here
        self.ui = QuizInterface(self)
        self.ui_started = False

    # leave as it is ...
    def still_has_questions(self):
        return not self.cancelled and self.question_number < len(self.question_list)

    def next_question(self):
        if not self.still_has_questions():
            self.high_score = max(self.high_score, self.score)
            self.ui.show_finished()
            return

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # make the UI display the question
        self.ui.display_question(
            self.current_question.text,
            self.score,
            self.high_score,
            self.question_number,
            len(self.question_list),
        )

        # user_answer = input(
        #     f"Q.{self.question_number}: {self.current_question.text} (True/False): "
        # )  # change this line and make the UI get the input from clicking on the images (false and true inside /images)
        if not self.ui_started:
            self.ui_started = True
            self.ui.run()

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print("You got it right!")
            # instead display an emoji like this (🎉) big on top of the question ... make it pop lol and make the UI class do that
            self.ui.show_feedback("🎉", True)
        else:
            # print("That's wrong.")
            # same as above but instead display this emoji red cross (❌) big on top of the question ... make it pop lol and make the UI class do that as well
            self.ui.show_feedback("❌", False)

        # update the score and question number on the UI as well
        self.ui.update_progress(
            self.score,
            self.high_score,
            self.question_number,
            len(self.question_list),
        )
        # print(f"Your current score is: {self.score}/{self.question_number}")
        # this line and the next can disapear ...
        # print("\n")

        self.ui.schedule_next_question()

    def restart(self):
        self.score = 0
        self.question_number = 0
        self.current_question = None
        self.next_question()
