import random

print("Welcome to hangman! The theme is 'The dinasour world' 🦕")

words = ["Bird", "Dinasour", "Fossil", "Volcano", "Island", "Ocean", "Asteroid", "Lava", "Cave", "Rock"]

word = random.choice(words).lower()
guessed_letters = []
mistakes = 0
while(True):
    for l in word:
        if l not in guessed_letters:
            print('_ ', end='')
        else:
            print(l + ' ', end='')

    if (len(guessed_letters) == len(word)):
        print("\nYou guessed the world ✅ Legend!")
        break
    
    letter = input("\n").lower()

    if(letter == word):
        print("\nYou guessed the world ✅ Legend!")
        break
    if(letter in word and len(letter) > 0):
        if(letter not in guessed_letters):
            print(letter + " is found in the word. Congrats!")
            guessed_letters.append(letter)
    else:
        mistakes += 1
        if(mistakes >= 6):
            print("Game Over ❌ Maximum tries reached")
            break
        print("Wrong letter.. Mistakes: " + str(mistakes))
