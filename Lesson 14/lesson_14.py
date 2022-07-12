from art import logo, vs
from game_data import data
from random import choice
import os


def clear():
    return os.system('cls')


def show_logo():
    """Clear the terminal and show the logo"""
    clear()
    print(logo)


def pick_person():
    """Pick a random person from the data dictionary"""
    return choice(data)


person_1 = pick_person()
person_2 = pick_person()


def check_person(person_1, person_2):
    """Check if person_1 is not the same as the person_2"""
    while person_1 == person_2:
        person_2 = pick_person()
    return person_2


def show_game():
    """Clear the terminal, show the logo and the persons to compare"""
    show_logo()
    print(
        f"Compare A: {person_1['name']}, the {person_1['description']}, from {person_1['country']}")
    print(vs)
    print(
        f"Against B: {person_2['name']}, the {person_2['description']}, from {person_2['country']}")


score = 0
end = False

while not end:
    if person_1 == person_2:
        person_2 = check_person(person_1, person_2)
    show_game()
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == 'A' and person_1['follower_count'] > person_2['follower_count']:
        person_2 = pick_person()
        score += 1
    elif guess == 'B' and person_2['follower_count'] > person_1['follower_count']:
        person_1 = person_2
        person_2 = pick_person()
        score += 1
    else:
        show_logo()
        print(f"Sorry, that's wrong. Final score: {score}")
        end = True
