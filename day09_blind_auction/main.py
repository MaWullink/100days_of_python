from art import logo

print(logo)

dictionary = {}

while True:
    user_name = input("What is your name? ")
    
    user_price = int(input("How much do you want to bid? "))

    dictionary[user_name] = user_price

    more_people = input("Are there any others in the room? y/n ").lower()

    print("\n" * 10)

    if more_people == "n":
        break

winner = max(dictionary, key=dictionary.get)
max_value = dictionary[winner]

print(f"The winner is {winner} with a bid of {max_value}.")