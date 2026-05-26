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

profit = 0
turn_off = True


def generate_report():
    report = f"""
Water: {resources["water"]} ml
Milk: {resources["milk"]} ml
Coffee: {resources["coffee"]} g
Profit: ${profit}
"""
    return report


def check_resources(coffee_type):
    for resource in MENU[coffee_type]["ingredients"]:
        if resources[resource] < MENU[coffee_type]["ingredients"][resource]:
            return False, f"Not enough {resource}"
    return True, "Enough resources"


def make_coffee(coffee_type):
    for resource in MENU[coffee_type]["ingredients"]:
        resources[resource] -= MENU[coffee_type]["ingredients"][resource]


def calculate_money(coffee_type, paid):
    global profit

    cost = MENU[coffee_type]["cost"]

    if paid > cost:
        profit += cost
        refund = round(paid - cost, 2)
        return True, f"${refund} being refunded."

    elif paid == cost:
        profit += cost
        return True, "Perfect!"

    else:
        return False, f"Not enough money. Here is your ${paid} back."


while turn_off:
    answer = input("What would you like? espresso/latte/cappuccino: ")

    if answer == "off":
        print("Shutting down..")
        turn_off = False

    elif answer == "report":
        print(generate_report())

    else:
        success, message = check_resources(answer)
        print(message)

        if success:
            print("Insert coins")

            quarters = int(input("Quarters: ") or 0)
            dimes = int(input("Dimes: ") or 0)
            nickles = int(input("Nickles: ") or 0)
            pennies = int(input("Pennies: ") or 0)

            paid = (
                quarters * 0.25 +
                dimes * 0.10 +
                nickles * 0.05 +
                pennies * 0.01
            )

            enough_money, message2 = calculate_money(answer, paid)
            print(message2)

            if enough_money:
                print("Making your coffee...")
                make_coffee(answer)
                print(generate_report())
                print(f"Here is your {answer}, Enjoy!")
            

                

            




  

