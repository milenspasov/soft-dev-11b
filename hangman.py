import random

print("Welcome to Hangman! ")
words = ["ESTATE", "INCEPTION", "AMELIE", "GATSBY", "SHAKESPEARE", "SPOTLESS", "SOCIETY", "SEIZE", "INTERSTELLAR", "FICTION"]
chosen = random.choice(words)
gameword = list(range(len(chosen)))
wrong = 0
sum1 = 0
str = ''
for i in range(len(chosen)):
    gameword[i] = "_ "

print("_ "*len(chosen))

while wrong <= 6:
    print("Guess your letter: ")
    letter = input()
    while letter.isalpha() == False or len(letter) > 1:
        print("You shoud type a letter.")
        print("Guess your letter: ")
        letter = input()
        
    if letter in chosen:
        for j in range(len(chosen)):
            if letter == chosen[j]:
                gameword[j] = letter + " "
                sum1 = sum1 + 1

        
        print(str.join(gameword))
        str = ''
    else:
        print("Incorrect!")
        wrong = wrong + 1

    def listToString(s): 
        str1 = ""  
   
        return (str1.join(s)) 
        
    if sum1 == len(chosen):
        print("You won!")
        break
