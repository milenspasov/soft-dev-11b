import random

list = ["saw", "room", "pig", "skeleton", "blood", "trap", "fridge", "cage", "chair", "toilet"]
rand = random.choice(list)
wrong = 0

guessed = "" 
fail = 0

print("_" * len(rand))

while fail < 6:
    letter = input("Guess your letter: ")
    if letter in rand:
        guessed += letter

        for element in rand:
            if element in guessed:
                print(element, end = '')
            else:
                print("_", end = '')
                wrong += 1

        print("")

        if wrong == 0:
            print("You win!")
            break
            
        wrong = 0
        
    else:
        print("Incorrect!")
        fail += 1
    
    if fail == 6:
        print("You lose, the word was", rand)
