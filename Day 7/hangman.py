import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = ['_' for i in chosen_word]

while '_' in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives -= 1
    if lives == 0:
        print(stages[lives])
        print("You Lose")
        break
    print(f"{' '.join(display)}")
    print(stages[lives])


if '_' not in display:
    print("You won")


