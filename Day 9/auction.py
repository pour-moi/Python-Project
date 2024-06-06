from art import logo

bid = []

def add_bidder(name, amount):
    bid.append({
        "name": name,
        "bid": amount
    })

print(logo)
print("Welcome to the secret auction program.")

next_bidder = True
while next_bidder:
    name = input("What is your name? ")
    amount = int(input("What is you bid? "))

    add_bidder(name, amount)
    choice = input("Are there any other bidders? Type 'y' or 'n' ")
    if choice == 'n':
        next_bidder = False

max_bid = 0  
bidder = ""
for amount in bid:   
    if max_bid < amount["bid"]:
        max_bid = amount["bid"]
        bidder = amount["name"]
    
print(f"The winner is {bidder} with the amount of ${max_bid}")
