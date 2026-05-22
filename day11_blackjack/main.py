from art import logo
import random

player_cards = []
computer_cards = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(number):
    return random.sample(cards, number)


def calculate_score(card_list):
    total_score = sum(card_list)
    
    if 11 in card_list and total_score > 21:
        card_list.remove(11)
        card_list.append(1)
        total_score = sum(card_list)

    return total_score


def show_hand(card_list):
    total_score = calculate_score(card_list)
    players_hand = ",".join(str(card) for card in card_list)

    print(f"Your hand: {players_hand}")
    print(f"Your total score: {total_score}")

    return total_score


def show_dealer(card_list):
    total_score = calculate_score(card_list)
    dealers_hand = ",".join(str(card) for card in card_list)

    print(f"Dealer's hand: {dealers_hand}")
    print(f"Dealer's total score: {total_score}")

    return total_score


play = input("Do you want to play a game of blackjack? 'y'/'n' ")

if play == "y":
    print(logo)

    player_cards += draw_card(2)
    computer_cards += draw_card(2)

    total_score = show_hand(player_cards)
    print(f"Dealer's first card: {computer_cards[0]}")

    playing = True

    while playing:

        if total_score == 21:
            print("Blackjack! You win.")
            break

        another_round = input("Do you want to hit? 'y'/'n' ")

        if another_round == "y":
            player_cards += draw_card(1)

            total_score = show_hand(player_cards)
            print(f"Dealer's first card: {computer_cards[0]}")

            if total_score > 21:
                print("You lose (bust)")
                playing = False

        elif another_round == "n":
            total_dealer = calculate_score(computer_cards)

            while total_dealer < 17:
                computer_cards += draw_card(1)
                total_dealer = calculate_score(computer_cards)

            show_dealer(computer_cards)

            if total_dealer > 21:
                print("Dealer busts, you win")
            elif total_score > total_dealer:
                print("You win")
            elif total_score == total_dealer:
                print("Draw")
            else:
                print("You lose")

            playing = False