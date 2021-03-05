from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
  Q = q['text']
  A = q['answer']
  question_bank.append(Question(Q,A))

QB = QuizBrain(question_bank)
for j in range(len(question_bank)):
  QB.next_question(j,question_bank)
