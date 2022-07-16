from tkinter import *


def button_clicked():
    converted_label['text'] = int(input.get()) * 1.609


window = Tk()
window.title("My first GUI Program")

input = Entry()
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
