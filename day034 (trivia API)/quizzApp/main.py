from question_model import Question
from quiz_brain import QuizBrain
import html
import json
from urllib.request import urlopen

question_bank = (
    []
)  # get the questions from this api : https://opentdb.com/api.php?amount=10&category=20&type=boolean

API_URL = "https://opentdb.com/api.php?amount=10&category=20&type=boolean"


with urlopen(API_URL, timeout=10) as response:
    question_data = json.load(response)["results"]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(html.unescape(question_text), question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

# leave this part of the code as it is, i want the brain to call the ui from the inside (of quiz_brain)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

## more instructions HERE !!
## just tested it and i love it but i actually want something else done to it ... i want to restart the game at the end of the game ... so when i press the victory emoji i want it to restart the game and keep the highscore between the current score and the number of questions ... in the same line basicaly
## keep the changes i made to it tho ... i like it as is i just want those small changes ..
