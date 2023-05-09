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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global check_mark
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer.config(text="Timer")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer(reps=0):
    global Timer
    global check_mark
    check = 0
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 0:
        Timer.config(fg=GREEN, text="WORK")
        countdown(work_sec)
    elif reps in [1, 3, 5]:
        check += 1
        check_mark.config(text=f"{'✔' * check}")
        Timer.config(fg=RED, text="Break")
        countdown(short_break_sec)
    elif reps in [2, 4, 6]:
        Timer.config(fg=GREEN, text="WORK")
        countdown(1 * 60)
    else:
        Timer.config(fg=RED, text="BIG BREAK")
        countdown(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        reps += 1
        start_timer(reps)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)

# canvas.create_text(100, 20, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
# image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# check mark
check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_mark.grid(column=1, row=2)

# Timer
Timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
Timer.grid(column=1, row=0)

# button
btn_start = Button(text="start", command=start_timer)
btn_start.grid(column=0, row=2)
btn_reset = Button(text="Reset", command=reset)
btn_reset.grid(column=2, row=2)

window.mainloop()
