from tkinter import *
from numpy import flip
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

try:
    data = pandas.read_csv("lesson 31/data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("lesson 31/data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=show_back)


def show_back():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back)


def is_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("lesson 31/data/to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=show_back)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="lesson 31/images/card_front.png")
card_back = PhotoImage(file="lesson 31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 68, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="lesson 31/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="Lesson 31/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_know)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
