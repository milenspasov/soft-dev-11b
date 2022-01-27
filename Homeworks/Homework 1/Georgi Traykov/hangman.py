import random
from re import A
import secrets

#welcoming message
print ("Welcome to Hangman!")

#list of 10 words
words_list = ["COFFEE", "SNAKE", "ROUTER", "PROTEIN", "OVERCOOKED", "ODDITY", "PORCELAIN", "SCREENSHOT", "PERFUME", "WIDOW"]
turns = 6
guessed = False

#an empty list that holds the guessed characters
guessed_letters = []
guessed_correctly = 0

selected_word = random.choice(words_list)
#print (selected_word) #махнете коментара за да се output-ва думата, по-лесно се проверява коя е
print ('_' * len(selected_word), end = '')

while not guessed and turns > 0:
    
    #if not guessed_letters:
        #print('\n') 
        #guess = input("Guess your letter:").upper()
    #else:
    guess = input("\nGuess your letter:").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You guessed this letter already.")
            
        elif guess not in selected_word:
            print("Incorrect!")
            turns -= 1
            guessed_letters.append(guess)
            for char in selected_word:
                if char in guessed_letters:
                    print(char, end = '')
                        
                else:
                    print("_", end = '')
        else:
            guessed_letters.append(guess)
            for char in selected_word:
                if char in guessed_letters:
                    print(char, end = '')
                    if char == guess:
                        guessed_correctly += 1         
                else:
                    print("_", end = '')
            if len(selected_word) == guessed_correctly:
                guessed = True
    else:
        if guess.isalpha() == False:
            print("Enter a letter!")
        elif len(guess) > 1:
            print("Please enter a single letter!")

if guessed == True:
    print("\nCongratulations, you won!")
else:
    print("\nYou lost, better luck next time!")