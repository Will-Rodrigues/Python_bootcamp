from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Brain 2.0")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Score Label
        self.score_label = Label(text=f'Score: ', background=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.card_word = self.canvas.create_text(150, 125, width=270, text="Ipsum Literis", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        # Buttons
        false_img = PhotoImage(file="lesson 34/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, background=THEME_COLOR, command=self.set_false)
        self.false_button.grid(column=0, row=2)
        true_img = PhotoImage(file="lesson 34/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, background=THEME_COLOR, command=self.set_true)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.card_word, text=q_text)
        else:
            self.canvas.itemconfig(self.card_word, text="The End")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def set_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def set_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
