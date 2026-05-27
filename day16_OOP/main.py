from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False

while not turn_off:

    answer = input(f"What would you like? {menu.get_items()}: ")

    if answer == "off":
        print("Shutting down..")
        turn_off = True

    elif answer == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(answer)

        if drink is not None:

            if coffee_maker.is_resource_sufficient(drink):

                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


