MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Report the resources of the machine"""
    print(f"{resources['water']}ml of water left.")
    print(f"{resources['milk']}ml of milk left.")
    print(f"{resources['coffee']}g of coffee left.")
    print(f"${money} in the machine")


def check_resource(order):
    """Check if the machine has enough ingredients for the order"""
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Make the conversion of the number of coins for the value of them"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennys = int(input("How many pennys?: ")) * 0.01
    return quarters + dimes + nickels + pennys


def check_transaction(inserted_money, order):
    """Check if the money is enough for the order"""
    global make_coffe
    if inserted_money < (MENU[order]["cost"]):
        print(f"It's not enough money. Here is your ${inserted_money} back")
        return 0
    else:
        change = inserted_money - MENU[order]["cost"]
        if change > 0:
            print(f"Here is your change of ${change}")
            make_coffe = True
            return inserted_money - change
        else:
            make_coffe = True
            return inserted_money


make_coffe = False
is_on = True

while is_on:
    make_coffe = False
    order = input("What would you like?\n(espresso/latte/cappuccino)\n")
    if order == 'report':
        report()
    elif order == 'off':
        quit()
    else:
        if check_resource(order):
            inserted_money = process_coins()
            money += check_transaction(inserted_money, order)
            print(make_coffe)
            if make_coffe == True:
                print(f"Enjoy you {order}")
                for resouce in resources:
                    if resouce in MENU[order]["ingredients"]:
                        resources[resouce] -= MENU[order]["ingredients"][resouce]
