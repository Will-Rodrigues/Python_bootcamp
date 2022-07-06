#1. Make the imports and setups

from random import randint

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

game_pos = [rock, paper, scissors]

#2. Show the welcome message and explain the rules

print("!!!Welcome to the rock-paper-scissors game!!!")
print("In this game you have to choose between the numbers 0, 1 or 2, that corresponds to rock, paper and scirrors!")
print("Remember!\nRock wins scissors\nPaper wins rock\nScissor wins paper")

#3. Take the player choice

player_name = input("What's your name?\n")
player_choice = int(input("Rock, paper or scissors? (Type 0, 1 or 2)\n"))

if player_choice >= 0 and player_choice < 3:
    print(game_pos[player_choice])
else:
    print ("Wrong enter, I give you a random choice then")
    player_choice = randint(0, 2)
    print(game_pos[player_choice])

#4. Take the computer choice

computer_choice = randint(0, 2)

print(f"Computer chose\n{game_pos[computer_choice]}")

#5 Compare the choices

if player_choice == 0 and computer_choice == 2:
    print(f"You win!")
elif player_choice > computer_choice:
    print(f"You win!")
elif player_choice == computer_choice:
    print("It's a Draw")
else:
    print(f"Sorry, You lose!")

print(f"Game Over\nThanks for playing, {player_name}")