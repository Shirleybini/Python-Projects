BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
import pandas as pd
import random

words_file = pd.read_csv("data/french_words.csv")
data_dict = words_file.to_dict(orient = 'records')

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(data_dict)
    canvas.itemconfig(lang_text,text='French',fill = 'black')
    canvas.itemconfig(word_text,text=current_card['French'],fill = 'black')
    canvas.itemconfig(card_bg,image = french_img)
    
    flip_timer = window.after(3000,func = flip_card)
    
    
def flip_card():    
    canvas.itemconfig(lang_text,text='English',fill = 'white')
    canvas.itemconfig(word_text,text=current_card['English'],fill = 'white')
    canvas.itemconfig(card_bg,image = english_img)
    

def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    next_card()



window = Tk()
window.title("Flashy")
window.config(padx = 50, pady=50,background=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800, height=525,bg=BACKGROUND_COLOR, highlightthickness=0)
french_img = PhotoImage(file='images/card_front.png')
card_bg = canvas.create_image(400,262.5,image = french_img)
lang_text = canvas.create_text(400,150, text = 'Language', fill='black', font=('Arial',40,'italic'))
word_text = canvas.create_text(400,263, text = 'Word', fill='black', font=('Arial',60,'bold'))
        
canvas.grid(row = 0, column = 0, columnspan = 2)

english_img = PhotoImage(file='images/card_back.png')
    
    
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0,command = next_card)
wrong_button.grid(row=1,column=0)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0,command = is_known)
right_button.grid(row=1,column=1)

next_card()


window.mainloop()



