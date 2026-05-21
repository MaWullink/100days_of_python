from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

result = float(input("What is your first number? "))

continue_calc = True

while continue_calc:

    operation = input("What operation do you want? '+' '-' '*' or '/' ")
    next_number = float(input("What is the next number? "))

    result = calculations[operation](result, next_number)
    print(f"Result: {result}")

    another = input("Do you want to continue? y/n ").lower()

    if another == "n":
        continue_calc = False
        print(f"Final result: {result}")