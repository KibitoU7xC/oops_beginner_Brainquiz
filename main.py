from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    question=i['text']
    answer=i['answer']
    new_question=Question(question,answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
