from random import choice
from art import logo
import os


def clear(): return os.system('cls')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]
    return choice(cards)


def game_begin():
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())


def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)


end = False
while not end:
    player_cards = []
    computer_cards = []
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        player_name = input("What's your name?: ")
        clear()
        print(logo)
        game_begin()
        if sum(player_cards) < 21 and sum(computer_cards) < 21:
            print(
                f"    {player_name}'s cards: {player_cards}, current score {calculate_score(player_cards)}")
            print(f"    Computer's first card: {computer_cards[0]}")
            while sum(player_cards) < 21:
                if sum(player_cards) == 21 or sum(player_cards) > 21:
                    break
                elif input("Type 'y' to hit or 'n' to pass: ") == 'y':
                    player_cards.append(deal_card())
                    print(
                        f"    {player_name}'s cards: {player_cards}, current score {calculate_score(player_cards)}")
                    print(f"    Computer's first card: {computer_cards[0]}")
                else:
                    break
            while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 18 and calculate_score(player_cards) < 21:
                computer_cards.append(deal_card())
        print(
            f"    {player_name}'s final hand: {player_cards}, final score {calculate_score(player_cards)}")
        print(
            f"    Computer's final hand: {computer_cards}, final score {calculate_score(computer_cards)} ")
        if calculate_score(player_cards) == calculate_score(computer_cards):
            print("It's a draw")
        elif calculate_score(player_cards) == 0 or calculate_score(computer_cards) > 21:
            print("You Win")
        elif calculate_score(computer_cards) == 0 or calculate_score(player_cards) > 21:
            print("You Lost")
        elif calculate_score(player_cards) > calculate_score(computer_cards):
            print("You Win")
        else:
            print("You Lost")
    else:
        end = True
