from game_data import data
from random import choice
from art import logo, vs

def start_game():
    a = choice(data)
    b = choice(data)
    game(a, b)

def check_result(user_choice, a, b):
    score = 0
    print(logo)
    if user_choice == 'a':
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"You are right! Your current score: {score}")
            a = b
            b = choice(data) 
            game(a, b)
        else:
            print(f"Sorry that's wrong :( Final score: {score}")
    
    if user_choice == 'b':
        if a["follower_count"] > b["follower_count"]:
            print(f"Sorry that's wrong :( Final score {score}")
        else:
            score += 1
            print(f"You are right! Your current score: {score}")
            a = b
            b = choice(data) 
            game(a, b)

print(logo)

def game(a, b):
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    check_result(user_choice, a, b)

start_game()