import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
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

user_choice = int(input("What do you choose? Type 0  for Rock, 1 for Paper or 2 for Scissors "))

computer_choice = random.randint(0, len(choice))

if user_choice == 0 and computer_choice == 1 or user_choice == 1 and  computer_choice == 2 or user_choice == 2 and computer_choice == 0:
    print(f"{choice[user_choice]}\nComputer Chose{choice[computer_choice]}\nYou Lose!!")
elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
    print(f"{choice[user_choice]}\nComputer Chose{choice[computer_choice]}\nYou Won!!")
elif user_choice > 3 or user_choice < 0:
    print("Please enter number 0, 1 or 2")
else:
    print(f"Your chose\n {choice[user_choice]} \nComputer Chose\n{choice[computer_choice]}\n Draw") 
