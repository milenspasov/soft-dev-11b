import random


def chooseWord(wordlist):
    return random.choice(wordlist)

# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    if c == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans



def getAvailableLetters(lettersGuessed):
    import string
    ans = list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)

def hangman(secretWord):
    print("Welcome to Hangman!")
    print("The word is",len(secretWord),"letters long.")
    
    global lettersGuessed
    mistakeMade = 0
    lettersGuessed = []
    
    while 6 - mistakeMade > 0:
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have", 6 - mistakeMade, "guesses left.")
            guess = str(input("Please guess a letter: ")).lower()
            
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
                
            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
                
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
                
        if 6 - mistakeMade == 0:
            print("-------------")
            print("You lost. The word is.",secretWord)
            break
        
        else:
            continue
wordlist = ["based", "poggers", "monke", "javascript", "zhabaskript", "piton", "oblak", "apple", "kola", "kartina"]

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
