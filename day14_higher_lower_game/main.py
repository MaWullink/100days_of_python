from art import logo, vs
import random
from game_data import data

print(logo)


def get_random_obj():
    objectA = random.choice(data)
    objectB = random.choice(data)

    while objectA == objectB:
        objectB = random.choice(data)

    return objectA, objectB


def check_answer(answer, objectA, objectB, score):
    if answer == "B" and objectB["follower_count"] > objectA["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        return True, score
    elif answer == "A" and objectA["follower_count"] > objectB["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
        return True, score
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        return False, score


def play_game():
    score = 0
    playing = True
    objectA, objectB = get_random_obj()
    while playing:
        print("\n"
            f"Compare A: {objectA['name']}, "
            f"a {objectA['description']}, "
            f"from {objectA['country']}."
        )

        print(vs)

        print(
            f"Against B: {objectB['name']}, "
            f"a {objectB['description']}, "
            f"from {objectB['country']}."
        )

        answer = input("\n""Who has more followers? Type 'A' or 'B': ").upper()

        playing, score = check_answer(answer, objectA, objectB, score)
        if playing:
            if objectB["follower_count"] > objectA["follower_count"]:
                objectA = objectB
                _, objectB = get_random_obj()
            else:
                _, objectB = get_random_obj()


play_game()