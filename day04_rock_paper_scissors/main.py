import random

rock = '''
    _______
---'   ____)
      (_____ )
      (_____ )
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

choice = [rock, paper, scissors]

player_choice = int(input("Choose rock (0), paper (1), or scissors (2): "))
computer_choice = random.randint(0, 2)

print("\nYou chose:")
print(choice[player_choice])

print("Computer chose:")
print(choice[computer_choice])

if player_choice == computer_choice:
    print("Draw")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win")
else:
    print("You lose")