import random

words = ["suspicious", "pointer", "bronze", "games", "samsung", "turkey", "water"]
word = random.choice(words)

print("Welcome to Hangman!")

allowed_tries = 6
guesses = []

game = False

while game == False:

    guess = input("Guess your letter: ")
    guesses.append(guess)

    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")

    if guess not in word:
        allowed_tries -= 1
        if allowed_tries == 0:
            break

    game = True

    for letter in word:
        if letter not in guesses:
            game = False

if game == True:
    print(f"You guessed the word! It was '{word}'")
else:
    print(f"You failed. The word was {word}.")
