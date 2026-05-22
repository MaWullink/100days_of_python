from art import logo
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def check_guess(guess, number):
    if guess < number:
        print("Too low.")
        return False
    elif guess > number:
        print("Too high.")
        return False
    else:
        print(f"You got it! The answer was {number}")
        return True


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        is_correct = check_guess(guess, number)

        if is_correct:
            return

        attempts -= 1

        if attempts == 0:
            print(f"You've run out of guesses. The number was {number}.")
        else:
            print("Guess again.")


playing = True

while playing:
    play_game()

    again = input("Want to play another game? 'y'/'n': ").lower()
    if again == "n":
        playing = False

      
    
    