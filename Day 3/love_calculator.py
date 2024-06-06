print("Welcome to the love calculator")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()
combined_name = name1 + name2

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

love = str(l+o+v+e)
true = str(t+r+u+e)
final_result = int(f"{true}{love}")

if final_result < 10 or final_result > 90:
    print(f"Your score is {final_result}, you go together like coke and mentos")
elif final_result > 40 and final_result < 50:
    print(f"Your socre is {final_result}, you are alright together.")
else:
    print(f"Your score is {final_result}")