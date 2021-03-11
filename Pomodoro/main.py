from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(TIMER)
    timer.config(text="TIMER",fg= GREEN)
    canvas.itemconfig(timertext, text='00:00')
    tick.config(text="")
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    REPS += 1
    
    
    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="20min BREAK",fg=RED)
        print(REPS,"Long Break")
        
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="5min BREAK",fg=PINK)
        print(REPS,"Short Break")
        
    else:
        countdown(work_sec)
        timer.config(text="WORK 25min",fg= GREEN)
        print(REPS,"WORK")
            
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    time_min = str(count//60)
    time_sec = str(count%60)
    if len(time_sec)==1:
        time_sec = '0'+ time_sec   
    
    Time = time_min+":"+time_sec
    canvas.itemconfig(timertext,text=Time)
    
    if count>0:
        global TIMER
        TIMER = window.after(1000,countdown,count-1)
        
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✔"
        tick.config(text = mark)
        
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image = tomato_img)
timertext = canvas.create_text(100,130, text = '00:00', fill='white', font=(FONT_NAME,20,'bold'))
canvas.grid(row=1,column=1)

timer = Label(text = "TIMER", font = (FONT_NAME,25,'bold'), fg=GREEN, bg=YELLOW)
timer.grid(row=0,column=1)

start = Button(text = "Start", font = (FONT_NAME,10), highlightthickness=0, command=start_timer)
start.grid(row=2,column=0)

reset = Button(text = "Reset", font = (FONT_NAME,10), command=reset_timer)
reset.grid(row=2,column=2)

tick = Label(text = "", font = (FONT_NAME,10), fg = GREEN, bg = YELLOW)
tick.grid(row=3,column=1)


window.mainloop()