import random

names = input("Give me everybody's names, seperated by a comma. ")
name_list = names.split(",")
# random_number = random.randint(0, len(name_list) - 1)

print(f"{random.choice(name_list)} is going to buy the meal today ")