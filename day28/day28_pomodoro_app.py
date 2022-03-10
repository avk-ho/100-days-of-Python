# https://www.udemy.com/course/100-days-of-code/learn/lecture/20887024#search

# Day 28

# Pomodoro App
# https://en.wikipedia.org/wiki/Pomodoro_Technique
# 25min work sessions followed by 5min breaks
# after 4 work sessions, the break is 20min instead of 5min

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER = None
REPS = 0
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS, TIMER
    REPS = 0
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks_label.config(text="")
    window.after_cancel(TIMER)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS, check_mark_text

    # work_sec = 11
    # short_break_sec = 5
    # long_break_sec = 10
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 == 0:
        title_label.config(text="Work")
        count_down(work_sec)
    else:
        check_mark_text += CHECK_MARK
        check_marks_label.config(text=check_mark_text)
        if REPS % 7 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        else:
            title_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS, TIMER
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    count_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        REPS += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28/tomato.png")
canvas.create_image(102, 112, image=tomato_img) # coordinates are roughly half the size of the canvas (to center the image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

check_mark_text = ""
check_marks_label = Label(text=check_mark_text, font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN)
check_marks_label.grid(column=1, row=3)

start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(column=2, row=2)

window.mainloop()