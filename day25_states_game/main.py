from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

map_turtle = Turtle()
map_turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")

guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed)}/50 States Correct",
        prompt="What's another state name?"
    ).title()

    if answer_state == "Exit":
        missing_states = [state for state in data["state"].values if state not in guessed]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    for state in data["state"]:
        if answer_state == state and state not in guessed:
            row = data[data.state == state]
            writer.goto(row["x"].item(), row["y"].item())
            writer.write(state)

            guessed.append(state)
            break

screen.exitonclick()
