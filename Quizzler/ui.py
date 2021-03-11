from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()

        self.window.title("Quizzler")
        self.window.config(padx = 20, pady=20,background=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250)
        self.ques_text = self.canvas.create_text(150,100,width = 250,text = "question here",font=('Arial',15,'italic'))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 20)

            
        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0,command = self.false_button)
        self.wrong_button.grid(row=2,column=1)
        
        right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right, highlightthickness=0,command = self.true_button)
        self.right_button.grid(row=2,column=0)

        self.score = Label(text = "Score: ",font = ('Arial',10),bg = THEME_COLOR, fg = 'white' )
        self.score.grid(row = 0, column = 1)
        
        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text,text = q_text)
        
        else:
            self.canvas.itemconfig(self.ques_text,text = "You are out of questions")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state= "disabled")
            
    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
        
        
    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)
        
        
    def feedback(self,answer):
        if answer:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        
        self.window.after(500,self.get_next_question)