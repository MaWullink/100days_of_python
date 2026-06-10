from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Support your favorite turtle!",
    prompt="Which colored turtle do you bet on?"
)

colors = ["green", "yellow", "purple", "orange", "pink", "blue"]
y_positions = [0, 25, 50, -25, -50, 75]

all_turtles = []

for i in range(len(colors)):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-210, y=y_positions[i])
    all_turtles.append(turtle)

race_on = True

while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 210:
            race_on = False
            winner_color = turtle.pencolor()

            if winner_color == user_bet:
                print("You win!")
            else:
                print(f"You lose! {winner_color} won.")

            break

screen.exitonclick()