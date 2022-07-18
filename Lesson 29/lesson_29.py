from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

def get_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    especial_chars = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]

    random_letters = [choice(letters) for _ in range(0, randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(0, randint(2, 4))]
    random_especial = [choice(especial_chars) for _ in range(0, randint(2, 4))]    
    password = random_letters + random_numbers + random_especial

    shuffle(password)
    final_result = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, final_result)


def save():
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()

    if len(password) < 1 or len(username) < 1 or len(website) < 1:
        messagebox.showinfo(
            title="Oooops", message="Please, dont't leave any fields empty")
    else:
        if messagebox.askokcancel(title=f"{website}", message=f"These are the details entered:\nEmail:{username}\nPassword: {password}\nIt's ok to save it?"):
            with open(f"lesson 29/passwords.txt", 'a') as data:
                data.write(f"{website} / {username} / {password}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="lesson 29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, columnspan=2, row=2)
username_entry.insert(0, "example@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=get_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
