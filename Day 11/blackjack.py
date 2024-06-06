from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_card = [random.choice(cards) ,random.choice(cards)]
computer_card = [random.choice(cards), random.choice(cards)]

play_game = True

def check_score(scores):
    result = 0
    for score in scores:
        result += score
    return result


def black_jack():
    print(logo)
    my_score = check_score(user_card)
    print(f"Your cards:{user_card}, current score: {my_score}")
    print(f"Computers first card: {computer_card[0]}")

    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'y':
        user_card.append(random.choice(cards))
        user_score = check_score(user_card)
        print(f"Your cards: {user_card}, current score {user_score}")
        computer_score = check_score(computer_card)
        check_winner(user_score, computer_score)  
        if user_score < 21:
            black_jack()
    else:
        computer_score = check_score(computer_card)
        print(computer_score)
        while computer_score < 21:
            computer_card.append(random.choice(cards))
            final_computer_score = check_score(computer_card)
            if final_computer_score == 21:
                    print("Computer Won") 
                    return        
            elif final_computer_score > 21:
                    print(f"Computer's final hand {computer_card}, finalscore {final_computer_score}")
                    print("You won")
                    return


def check_winner(user_score, computer_score):
    if user_score == computer_score:
        print("Draw")
    if user_score <= 21 and user_score > computer_score:
        print("You won")
    if user_score > 21:
        print(f"Your final hand is: {user_card}, final score: {user_score}")
        print("You Lose")


play = input("Do you want to play a game of BlackJack? Type 'y' or 'n' ")
if play == "y":
    black_jack()