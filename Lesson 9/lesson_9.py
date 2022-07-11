import os

clear = lambda: os.system('cls')

print("Welcome to the secret auction program.")

bids = {}


def get_bid(user_name, user_bid):
    bids[user_name] = user_bid


end = False
while not end:
    user_name = input("What is your name?\n")
    user_bid = float(input("What's your bid?\n$"))
    get_bid(user_name, user_bid)
    go_on = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if go_on == 'yes':
        clear()
    else:
        clear()
        print(
            f"The winner is {max(bids, key=bids.get)}, with the bid of ${max(bids.values())} ")
        end = True
