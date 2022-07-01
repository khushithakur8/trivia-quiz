class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questionlist = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < 12:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questionlist[self.question_number]
        self.question_number += 1
        print()
        user_ans = input(f"Q{self.question_number}. {current_question.question} (True/False) ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("Wrong answer !")
            print(f"The correct answer was {correct_ans}")
            print(f"Your current score {self.score}/{self.question_number}")

    print("You have completed the quiz")

    def final_score(self):
        print(f"Your final score is {self.score}/{self.question_number}")



