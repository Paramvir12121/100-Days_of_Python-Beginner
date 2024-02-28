from question_model import Question
from quiz_brain import QuizBrain
import requests

parameters = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")

data = response.json()
question_data =  data["results"]

question_bank = []

for Q in question_data:
    question_text = Q["question"]
    question_answer = Q["correct_answer"]
    new_question = Question(question_text, question_answer)
    #print(new_question.text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question() is True:
    quiz.next_question()

print("\n\nYou have completed the quiz!!!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
