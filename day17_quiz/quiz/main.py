from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for Q in question_data:
    question_text = Q["text"]
    question_answer = Q["answer"]
    new_question = Question(question_text, question_answer)
    #print(new_question.text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question() is True:
    quiz.next_question()
