import random

word_list = ["cobra", "boa", "adder", "viper", "mamba", "taipan", "hognose", "kingsnake", "boiga", "serpent"]
tries = 6 
random_word = random.choice(word_list)

#print(random_word)
print("\nWelcome to Hangman!\n")

final = []
for i in random_word:
     final += "_"

while(tries):
     count = 1
     for i in final:
          print(i, end=" ")

     #User input
     letter = input("\nGuess your letter: ")

     for i in range(len(random_word)):
          if(random_word[i]==letter):
               final[i] = random_word[i]
               count = 0

     #Проверки за оставащ брой опити и въведени грешни букви
     if(count == 1):
          tries -= 1
          if(tries == 0):
               print("\nTake the L!")
               print("The word was: " + random_word)
               break
          else:
               print("Incorrect! Tries left: " + str(tries))

     #Проверка за липсващи букви
     if("_" not in final):
          print(random_word)
          print("\nYou Won!")
          break