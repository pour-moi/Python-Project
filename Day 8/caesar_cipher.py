from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    word = ""
    for letter in text:
        if letter in alphabet:
            index_num = alphabet.index(letter)
            if direction == "encode":
                word += alphabet[(index_num + shift) % len(alphabet)]
            elif direction == "decode":
                word += alphabet[(index_num - shift) % len(alphabet)]
        else:
            word += letter  
    print(word) 

print(logo)
start = True
while start:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)

    choice = input("Type 'yes' if you want to go again. otherwise type 'no' ")
    if choice == 'no':
        print("Good bye")
        start = False

   