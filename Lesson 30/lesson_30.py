from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


def get_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
               "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }

    if len(password) < 1 or len(username) < 1 or len(website) < 1:
        messagebox.showinfo(
            title="Oooops", message="Please, dont't leave any fields empty")
    else:
        try:
            with open("lesson 30/passwords.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("lesson 30/passwords.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("lesson 30/passwords.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("lesson 30/passwords.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="No Data File Found", message="Please, save any password before trying to search")
    else:
        if website in data:
            username = data[website]['username']
            password = data[website]['password']
            messagebox.showinfo(
                title=website, message=f"Username: {username}\nPassword: {password}")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Column 0
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Column 1
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="lesson 29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, columnspan=2, row=2)
username_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, columnspan=2, row=4)

# Column 2
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

generate_password_button = Button(
    text="Generate Password", command=get_password)
generate_password_button.grid(column=2, row=3)

window.mainloop()
