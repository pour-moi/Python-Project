import random

EASY = 10
HARD = 5

the_number = random.randint(1, 101)

def game(level):
    while level != 0:
        user_choice = int(input("Guess a numer from 1 - 100 "))
        if user_choice > the_number:
            print("Too high")
            level -= 1
            print(f"You have {level} attempts")
        elif user_choice < the_number:
            print("Too Low")
            level -= 1
            print(f"You have {level} attempts")
        elif user_choice == the_number:
            print(f"You got it the number is {the_number}")
            break

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard' ")

if level == 'easy':
    game(EASY)
else:
    game(HARD)