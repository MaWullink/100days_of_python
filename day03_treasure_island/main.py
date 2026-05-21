print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("A forgotten map leads you into dangerous territory.")
print("Your mission is to find the treasure... if you survive the journey.")

choice = input("You reach a fork in the path. Do you go left or right? ").lower()

if choice == "left":
    print("You follow the left path and arrive at the edge of a vast, silent lake.")
    swim = input("The water is dark. It almost looks red. Do you swim across or wait on the shore? ").lower()

    if swim == "swim":
        print("You dive into the water. The cold is immediate. Something moves beneath you...")
        print("Claws grip your ankles and drag you downward.")
        print("You try to scream, but a mixture of blood and water fills your lungs.")
        print("Pain fades into silence as darkness closes in around you.")

    elif swim == "wait":
        print("You wait. The water remains still, almost unnaturally calm.")
        print("After a while, a hidden passage opens and three ancient doors appear before you.")
        print("One red, one blue, and one that seems to shift color when you look at it.")

        door = input("Which door do you choose? (red/blue/yellow) ").lower()

        if door == "red":
            print("You step forward. Heat erupts instantly. Flames consume everything.")
        elif door == "blue":
            print("The moment you enter, the floor collapses into deep, freezing water.")
        elif door == "yellow":
            print("You step through the final door. The room is empty... then you see it.")
            print("A small scroll — another map.")
            print("You have come far, but your journey is not done yet...")
        else:
            print("You hesitate too long. The doors vanish. Darkness surrounds you.")

    else:
        print("You hesitate. The world around you fades into darkness.")

elif choice == "right":
    print("You take the right path into the forest.")
    print("You can feel eyes on your back — something is watching you silently.")
    print("Then an arrow pierces through your chest, straight through your heart.")
    print("You die instantly")

else:
    print("You stand still for too long. The path disappears beneath your feet.")
    print("There is nothing left but silence.")