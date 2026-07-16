from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):

        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR
        )


        # Score label
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR
        )

        self.score_label.grid(
            row=0,
            column=1
        )


        # Question canvas
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white"
        )

        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )

        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=50
        )


        # Buttons
        self.true_image = PhotoImage(
            file="./images/true.png"
        )

        self.false_image = PhotoImage(
            file="./images/false.png"
        )


        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_pressed
        )

        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_pressed
        )


        self.true_button.grid(
            row=2,
            column=0
        )

        self.false_button.grid(
            row=2,
            column=1
        )


        self.get_next_question()


        self.window.mainloop()



    def get_next_question(self):

        if self.quiz.still_has_questions():

            self.canvas.config(
                bg="white"
            )

            self.score_label.config(
                text=f"Score: {self.quiz.score}"
            )

            question = self.quiz.next_question()

            self.canvas.itemconfig(
                self.question_text,
                text=question
            )

        else:

            self.canvas.itemconfig(
                self.question_text,
                text=f"Quiz finished!\n\nScore: {self.quiz.score}/{self.quiz.question_number}"
            )

            self.true_button.config(
                state="disabled"
            )

            self.false_button.config(
                state="disabled"
            )



    def true_pressed(self):

        self.give_feedback(
            self.quiz.check_answer("True")
        )



    def false_pressed(self):

        self.give_feedback(
            self.quiz.check_answer("False")
        )



    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(
                bg="green"
            )

        else:
            self.canvas.config(
                bg="red"
            )


        self.window.after(
            1000,
            self.get_next_question
        )