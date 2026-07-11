from tkinter import *
import pandas

# -------------------- Variables -------------------- #

timer = None
current_word = None
learned_words = []


# -------------------- Data -------------------- #

df = pandas.read_csv("./data/japanese_words.csv", encoding="utf-8")


# -------------------- Save Progress -------------------- #

def save_progress():
    with open("./data/learned_words.txt", "w", encoding="utf-8") as file:
        for word in learned_words:
            file.write(word + "\n")


# -------------------- Button Functions -------------------- #

def handle_right():
    learned_words.append(current_word)
    save_progress()
    new_word()


def handle_wrong():
    new_word()


# -------------------- Flash Cards -------------------- #

def new_word():
    global timer
    global current_word

    # Stop old timer
    if timer:
        window.after_cancel(timer)

    # Remove words already learned. The ~ flips True and False
    available_words = df[~df["English"].isin(learned_words)]

    # If everything is learned
    if len(available_words) == 0:
        canvas.itemconfig(language_text, text="Finished!")
        canvas.itemconfig(word_text, text="All words learned 🎉")
        return

    # Pick random word
    random_row = available_words.sample().iloc[0]

    japanese_word = random_row["Japanese"]
    english_answer = random_row["English"]

    current_word = english_answer

    # Show Japanese
    canvas.itemconfig(language_text, text="Japanese")
    canvas.itemconfig(word_text, text=japanese_word)


    # Flip after 4 seconds
    def flip_card():
        canvas.itemconfig(language_text, text="English")
        canvas.itemconfig(word_text, text=english_answer)

    timer = window.after(4000, func=flip_card)



# -------------------- UI -------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Japanese Flash Cards")
window.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOR
)


# Canvas

canvas = Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

card_front = PhotoImage(file="./images/card_front.png")

canvas.create_image(
    400,
    263,
    image=card_front
)


language_text = canvas.create_text(
    400,
    150,
    text="Japanese",
    font=("Arial", 30, "italic")
)


word_text = canvas.create_text(
    400,
    263,
    text="",
    font=("Arial", 40, "bold")
)


# Buttons

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")


right_btn = Button(
    image=right_img,
    highlightthickness=0,
    command=handle_right
)

wrong_btn = Button(
    image=wrong_img,
    highlightthickness=0,
    command=handle_wrong
)


# Layout

canvas.grid(row=0, column=0, columnspan=2)

wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)


# Start first card
new_word()


window.mainloop()