import pandas
import datetime as dt
from random import choice
import smtplib as smtp

EMAIL = ''
PASS = ''

date_list = pandas.read_csv("lesson 32/birthdays.csv")
today = dt.date.today()

with open("lesson 32/letter_templates/letter_1.txt") as data:
    letter_1 = data.read()

with open("lesson 32/letter_templates/letter_2.txt") as data:
    letter_2 = data.read()

with open("lesson 32/letter_templates/letter_3.txt") as data:
    letter_3 = data.read()

letters = [letter_1, letter_2, letter_3]

for month in date_list.month:
    if month == today.month:
        possible_birthday = date_list[date_list.month == month]
        if int(possible_birthday.day) == today.day:
            choosed_letter = choice(letters)
            new_letter = choosed_letter.replace("[NAME]", possible_birthday.name.item())
            with smtp.SMTP("smtp.office365.com") as connection:
                connection.starttls()
                connection.login(EMAIL, PASS)
                connection.sendmail(from_addr=EMAIL, to_addrs=possible_birthday.email, msg=f"Subject:It's your birthday\n\n{new_letter}")
