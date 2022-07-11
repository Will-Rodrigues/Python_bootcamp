import random
from word_list import word_list
from pics import HANGMANPICS

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

player_lives = 6

while player_lives > 0:
    if "_" in display:
        print(HANGMANPICS[player_lives])
        print(display)
        guess = input("Guess a letter:\n").lower()
        letter_pos = 0
        if guess in chosen_word:
            if guess in display:
                print("You already have guessed this letter")
            else:
                for letter in chosen_word:
                    if letter == guess:
                        display.pop(letter_pos)
                        display.insert(letter_pos, letter)
                    letter_pos += 1
        else:
            print("You guessed wrong, you lose a life")
            player_lives -= 1
    else:
        print("You have won!")
        break

if player_lives == 0:
    print("You lose! Game Over")