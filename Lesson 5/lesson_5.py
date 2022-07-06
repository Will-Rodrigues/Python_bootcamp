import random

#1. Create a greetings message and explain the propose
print("Welcome to the PYssword Generator")
print("Here we will create an strong password for you, with the basic paramaters for your security.")

#2. Create the lists of characters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

especial_chars = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]

#3. Ask for the parameters
pass_letters = int(input("How many letters you like in your password?\n"))

pass_numbers = int(input("How many numbers you like in your password?\n"))

pass_especial = int(input("How many especial characters you like in your password?\n"))

#4. Do the magic

password = []

for letter in range (0, pass_letters):
    password.append(random.choice(letters))

for number in range (0, pass_numbers):
    password.append(random.choice(numbers))

for especial in range (0, pass_especial):
    password.append(random.choice(especial_chars))

random.shuffle(password)
final_result = ''.join(password)

#5. Show de password

print(f"Your password is: {final_result}")