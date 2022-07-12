from random import randint

EASY = 10
HARD = 5


def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
        return EASY
    else:
        return HARD


def check_guess(guess, SECRET_NUMBER, lifes):
    """Check the answer against guess. Return the number of turns remaing."""
    if guess > SECRET_NUMBER:
        print("Too high.")
        return lifes - 1
    elif guess < SECRET_NUMBER:
        print("Too low.")
        return lifes - 1
    else:
        print(f"You got it! The answer was {SECRET_NUMBER}.")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    SECRET_NUMBER = randint(1, 101)
    lifes = set_difficulty()

    guess = 0
    while guess != SECRET_NUMBER:
        if lifes > 0:
            print(f"You have {lifes} attempts")
            guess = int(input("Make a guess: "))
            lifes = check_guess(guess, SECRET_NUMBER, lifes)
        else:
            print(f"You lost, the number was {SECRET_NUMBER}.")
            return


game()
