from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="White", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="", width=280, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        x_img = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_img, highlightthickness=0, command=self.wrong)
        self.x_button.grid(column=1, row=2)

        v_img = PhotoImage(file="images/true.png")
        self.v_button = Button(image=v_img, highlightthickness=0, command=self.correct)
        self.v_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="THE END!")
            self.x_button.config(state="disabled")
            self.v_button.config(state="disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(2000, self.get_next_question)
