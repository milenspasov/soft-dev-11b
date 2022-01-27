import random

words = ["world", "sound", "classroom", "hangman", "butterfly", "shrink", "apple", "tree", "four", "bottle"]
strikes = 0
word = words[random.randint(0,9)]
word_progress="_ " * len(word)

print("Welcome to Hangman!")
print(word_progress)

while("_" in word_progress and strikes<6):
    word_list = list(word_progress)
    letter = str(input("Guess your letter: "))
    if(letter in word):
        if(letter in  word_progress):
            print("Letter already guessed!")
            continue
        
        for i in range(len(word)):
            if(word[i]==letter):
                word_list[i*2] = letter

        word_progress=''.join(word_list)
        print(word_progress)
    else:
        print("Incorrect!")
        strikes+=1

if(strikes==6):
    print("Game over! :(")
    print("The word was:", word)
else:
    print("You win!")
    print("The word was:", word)
