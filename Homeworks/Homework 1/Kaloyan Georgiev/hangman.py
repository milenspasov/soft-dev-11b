from random import randint
wordcount = 10
words = [
    "rat",
    "hall",
    "inn",
    "fortress",
    "algebra",
    "bulgarian",
    "seven",
    "fish",
    "hero",
    "murderer"
]

def check_guessed(guess):
    for i in guess:
        if i == "_":
            return False
    return True

#while True:
current = words[randint(0, wordcount-1)]
print("Your word has {0} letters:".format(len(current)))
guess_str = ""
for i in current:
    guess_str += "_"
    print("_", end="")
print("")
guessed = False
tries = 6
while not(guessed):
    guess = input("Enter your guess: ")
    while(len(guess) != 1):
        print("You can only guess 1 letter at a time")
        guess = input("Enter your guess: ")
    if guess in current:
        index = current.index(guess)
        if(guess_str[index] != "_"):
            index = current[index+1:].index(guess) + index + 1
        guess_str = guess_str[0:index] + guess + guess_str[index+1:len(current)+1]
        print("RIGHT")
    else:
        tries -= 1
        print("Wrong, you have {0} tries".format(tries))
    guessed = check_guessed(guess_str)
    if(guessed):
        print("Congratulations, the words was: " + guess_str)
        break
    print(guess_str)
    if(tries == 0):
        print("You lose")
        break

