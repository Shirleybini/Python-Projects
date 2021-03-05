class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0

  def next_question(self, q_number, q_list):
    Q = q_list[q_number]
    
    user_answer = input(f"Q.{q_number+1}: {Q.text} (True/False): ")
    if user_answer == Q.answer:
      self.score +=1
      print("You got it right!")

    else:
      print("That\'s wrong.")

    print(f"The correct answer was: {Q.answer}.")
    print(f"Your cuurect score is: {self.score}/{q_number+1}\n")

    q_number += 1

  