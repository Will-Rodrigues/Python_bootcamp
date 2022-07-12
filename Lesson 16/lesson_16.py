from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    items = menu.get_items()
    order = input(f"What would you like? ({items})\n")
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        is_on = False
    else:
        choice = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
