print("Welcome to python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
final_bill = 0

if size == "S":
    final_bill = small_pizza
    if add_pepperoni == "Y":
        final_bill = small_pizza + 2
    if extra_cheese == "Y":
            final_bill = small_pizza + 1
elif size == "M":
    final_bill = medium_pizza
    if add_pepperoni == "Y":
          final_bill = medium_pizza + 3
    if extra_cheese == "Y":
        final_bill = medium_pizza + 1
elif size == "L":
    final_bill = large_pizza
    if add_pepperoni == "Y":
        final_bill = large_pizza + 3
    if extra_cheese == "Y":
        final_bill = large_pizza + 1

print(f"Your final bill is {final_bill}") 
