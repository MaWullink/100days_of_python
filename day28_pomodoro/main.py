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

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps

    if reps in [0, 2, 4, 6]:
        title.config(text="Work", fg=GREEN)

        count_down(WORK_MIN * 60)


    elif reps in [1, 3, 5]:
        check_mark.config(text="✓" * reps)
        title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    elif reps == 7:
        title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer

    count_minutes = count // 60
    count_min = count % 60

    canvas.itemconfig(timer_text, text=f"{count_minutes:02}:{count_min:02}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps == 7:
            reset()
        else:
            reps += 1
            start()





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato)

timer_text = canvas.create_text(
    125, 145,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 25, "bold")
)

# Labels
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))

# Buttons
start_btn = Button(text="Start", command=start, highlightthickness=0)
reset_btn = Button(text="Reset", command=reset, highlightthickness=0)

# Layout
title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
check_mark.grid(row=3, column=1)
reset_btn.grid(row=2, column=3)

window.mainloop()