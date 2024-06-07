from game_data import data
from random import choice
from art import logo, vs

def start_game():
    a = choice(data)
    b = choice(data)
    score = 0
    game(a, b, score)

def check_result(user_choice, a, b):
    print(logo)
    if a["follower_count"] > b["follower_count"]:
        return user_choice == 'a'
    else:
        return user_choice == 'b'

print(logo)

def game(a, b, score):
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = check_result(user_choice, a, b)
    if result:
        score += 1
        print(f"You are right! Your current score: {score}")
        a = b
        b = choice(data) 
        game(a, b, score)
    else:
        print(f"Sorry that's wrong :( Final score {score}")


start_game()