class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_question = None
        self.user_answer = None
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        self.check_answer(self.user_answer,self.current_question.answer )
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it Right!!!")
            self.score +=1
        else:
            print("That's Wrong!")
        print(f"Corrent answer is {correct_answer}")
        print(f"Your Score is {self.score}/{self.question_number}")

        

        

        
            


        