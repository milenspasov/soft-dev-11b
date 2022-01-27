#importing the libraries
import random





#List of words.
word_list = ['vladika',
'fashizm',
'lego',
'batman',
'gelik',
'maibah',
'skyline',
'krajba',
'kottakoz',
'kukskuklan']

word = random.choice(word_list)
guessed_word = list('*'*len(word))
guessed_letters=[]



def replace(guess):
    replacing_indices=[index for index,value in enumerate(word) if value==guess]
    global guessed_word
    for i in replacing_indices:
            guessed_word[i]=guess
    


print('Welcome to Hangman!')
print('dumi = {}\n'.format(''.join(guessed_word)))





chance = 0
while not int(chance) in range(1,16):
    try:
        chance = int(input("kolko probi sakash za da poznaesh [1-15]"))
    except:
        print('sloji mejdu 1 do 15')
turn = 1






#Guessing begins
while turn<=chance:
    #prints the word and the guessed letters.
    print('\n dumata e ',''.join(guessed_word))
    print('Izpolzvani bukvi veche: ', ','.join(guessed_letters))
    guess = input("turn {}\t".format(turn))



 
    if guess in guessed_letters:
        print("poznal si q veche, izmudri druga\n")
        continue
    guessed_letters.append(guess)


    
  
    if guess == word:
        print("bratan, evala che prevurtq igrata")
        exit(0)
        


    if guess in word and len(guess)!=0:
        print('Vui! taq  bukwa {} q ima v dumata '.format(guess))
        replace(guess)
        
    else:
        print("LOSER")
        turn+=1

    if '*' not in guessed_word:
        print("Good job, respect++")
        exit(0)
    


print('LOSER')
exit(0)