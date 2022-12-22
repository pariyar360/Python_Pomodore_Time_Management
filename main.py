from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shortbreak_sec = SHORT_BREAK_MIN * 60
    longbreak_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(longbreak_sec)
        title.config(text="Break", foreground=RED)
    elif reps % 2 == 0 and reps % 8 != 0:
        count_down(shortbreak_sec)
        title.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        winsound.Beep(1000, 250)
        marks = ""
        sessions = math.floor(reps/2)
        print(sessions)
        for _ in range(sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)

# Title Label
title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), foreground=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

# Tomato Background
image_file = PhotoImage(file="tomato.png")
canvas.create_image(102, 113, image=image_file)
canvas.grid(column=1, row=1)

# Timer
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

# Reset Button
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

# Checkmark label
checkmark = Label(text="", bg=YELLOW, foreground=GREEN)
checkmark.grid(column=1, row=3)



window.mainloop()

