from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    new_ques = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(new_ques)

quizbrain = QuizBrain(question_bank)


while quizbrain.still_has_questions():
    quizbrain.next_question()

print("\n You've completed the quiz")
quizbrain.final_score()
