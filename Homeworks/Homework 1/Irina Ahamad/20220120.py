from hmac import digest
import random

def confusedFace():
    faces = [" ┛ಠДಠ)┛彡┻━┻", " (・_・ヾ", "(╯ಠ_ರೃ)╯", "( •́ ⍨ •̀)"]
    print(faces[random.randint(0, len(faces)-1)])

def hangman():
    print("Welcome to hangman!")
    words = ["monster", "eye", "stela", "terror", "paranoia", "fear", "nightmare", "anarchy", "blood", "tyrant"]
    word = words[random.randint(0, len(words)-1)]
    hiddenWord = "_"*len(word)
    progress = 0
    failedAttempts = 0
    while failedAttempts < 6 and progress < len(word):
        for l in range(len(word)):
            print(hiddenWord[l], end = " ")
        revealed = False
        letter = input("\nGuess your letter: ")
        for i in range(len(word)):
            if letter == word[i]:
                revealed = True
                # string acrobatics
                tempList = list(hiddenWord)
                tempList[i] = word[i]
                hiddenWord = ''.join(tempList)
                progress += 1
        if revealed == False:
            failedAttempts += 1
            print("Incorrect! Attempts left: " + str(6 - failedAttempts))
    if failedAttempts == 6:
        print("You lost : (")
        print("The word was: " + word + "\n")
    elif progress == len(word):
        print(hiddenWord)
        print("Congrats! You guessed the word (•̀ᴗ•́)൬༉\n")

def pyramid():
    print("Welcome to pyramid!")
    rows = input("rows = ")
    rows = int(rows)
    pyramid = [[]]
    for y in range(rows):
        for x in range(y+1):
            pyramid[y].append(random.randint(-100, 100))
            print(pyramid[y][x], end = " ")
        print()
        pyramid.append([])
    for y in range(rows-2, -1, -1):
        for x in range(len(pyramid[y])):
            pyramid[y][x] += max(pyramid[y+1][x], pyramid[y+1][x+1])
    print("The largest sum is " + str(pyramid[0][0]))
    return pyramid[0][0]

def usedLetter(letter, usedLetters):
    i = 0
    for i in range(len(usedLetter)):
        if letter == usedLetters[i]:
            return 1
    if i == len(usedLetters):
        return 0

def playfairEncrypt(matrix):
    message = input("Enter a message to encrypt: ")
    message = message.upper()

    # create a diagram for the message
    l = 0
    y = 0
    diagram = [[]]
    while l < len(message)-1:
        if l != 0:
            diagram.append([])
        if message[l] == message[l+1]:
            diagram[y].append(message[l])
            diagram[y].append("X")
            l += 1
        else:
            diagram[y].append(message[l])
            diagram[y].append(message[l+1])
            l += 2
        y += 1
    if len(message) % 2 == 1:
        diagram.append([])
        diagram[y].append(message[len(message)-1])
        diagram[y].append("X")

    print("Diagram :", end = " ")
    for i in range(len(diagram)):
        print(diagram[i][0] + diagram[i][1], end = " ")
    print()
    
    # encrypt the diagram
    for i in range(len(diagram)):
        # find the letters
        found = False
        for firstLetterY in range(5):
            for firstLetterX in range(5):
                if matrix[firstLetterY][firstLetterX] == diagram[i][0]:
                    found = True
                    break
            if found:
                break
        found = False
        for secondLetterY in range(5):
            for secondLetterX in range(5):
                if matrix[secondLetterY][secondLetterX] == diagram[i][1]:
                    found = True
                    break
            if found:
                break
        
        # see if the letters are on the same row
        if firstLetterY == secondLetterY:
            # get the letter on the right
            diagram[i][0] = matrix[firstLetterY][(firstLetterX+1)%5]
            diagram[i][1] = matrix[secondLetterY][(secondLetterX+1)%5]
        # see if the letters are in the same column
        elif firstLetterX == secondLetterX:
            # get the letter under
            diagram[i][0] = matrix[(firstLetterY+1)%5][firstLetterX]
            diagram[i][1] = matrix[(secondLetterY+1)%5][secondLetterX]
        # the letters form a rectangle
        else:
            diagram[i][0] = matrix[firstLetterY][secondLetterX]
            diagram[i][1] = matrix[secondLetterY][firstLetterX]
        
    print("Encrypted message:", end = " ")
    for i in range(len(diagram)):
        print(diagram[i][0] + diagram[i][1], end = "")
    print()

    return diagram

def playfairDecrypt(matrix):
    message = input("Enter a message to decrypt: ")
    message = message.upper()

    # divide the message
    l = 0
    y = 0
    diagram = [[]]
    while l < len(message)-1:
        if l != 0:
            diagram.append([])
        diagram[y].append(message[l])
        diagram[y].append(message[l+1])
        l += 2
        y += 1
    
    for i in range(len(diagram)):
        # find the letters
        found = False
        for firstLetterY in range(5):
            for firstLetterX in range(5):
                if matrix[firstLetterY][firstLetterX] == diagram[i][0]:
                    found = True
                    break
            if found:
                break
        found = False
        for secondLetterY in range(5):
            for secondLetterX in range(5):
                if matrix[secondLetterY][secondLetterX] == diagram[i][1]:
                    found = True
                    break
            if found:
                break
        
        # see if the letters are on the same row
        if firstLetterY == secondLetterY:
            # get the letter on the left
            diagram[i][0] = matrix[firstLetterY][abs((firstLetterX-1)%5)]
            diagram[i][1] = matrix[secondLetterY][abs((secondLetterX-1)%5)]
        # see if the letters are in the same column
        elif firstLetterX == secondLetterX:
            # get the letter above
            diagram[i][0] = matrix[abs((firstLetterY-1)%5)][firstLetterX]
            diagram[i][1] = matrix[(abs(secondLetterY-1)%5)][secondLetterX]
        # the letters form a rectangle
        else:
            diagram[i][0] = matrix[firstLetterY][secondLetterX]
            diagram[i][1] = matrix[secondLetterY][firstLetterX]
    
    # tackle the X cases
    for y in range(len(diagram)):
        if diagram[y][1] == "X":
            diagram[y][1] = ""

    print("Decrypted message:", end = " ")
    for i in range(len(diagram)):
        print(diagram[i][0] + diagram[i][1], end = "")
    print()

    return diagram

def playfairCypher():
    print("Welcome to Playfair cypher!")
    alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
    keyword = list("TUES")
    letterQueue = keyword + alphabet
    matrixQueue = [""*25]
    matrixQueue[0] = letterQueue[0]

    # remove the repeating letters
    for l in range(len(letterQueue)):
        # check if the current letter has appeared before in letterQueue
        for l2 in range(0, l):
            if letterQueue[l] == letterQueue[l2]:
                break
            if l2 == l - 1:
                matrixQueue.append(letterQueue[l])

    # make the matrix
    matrix = [[]]
    for y in range(5):
        for x in range(5):
            matrix[y].append(matrixQueue[y*5 + x])
            #print("matrixQueue[y*5 + x] = " + matrixQueue[y*5 + x])
        matrix.append([])

    # display the matrix
    for y in range(5):
        for x in range(5):
            print(matrix[y][x], end = " ")
        print()
    
    diagram = [[]]

    looping = True
    while looping:
        pick = input("Enter 1 to enrypt a message, 2 to decrypt or 0 to quit: ")
        if pick == "0":
            print("Goodbye ( ु⁎ᴗᵨᴗ⁎)ु.zZ")
            looping = False
        elif pick == "1":
            diagram = playfairEncrypt(matrix)
        elif pick == "2":
            diagram = playfairDecrypt(matrix)
        else:
            print("Please pick a valild option!")
            confusedFace()    
    print()
    return diagram

print("Welcome! :)")
print("Name: Irina Ahamad")
print("Class: 11b")
print("№: 13")

pick = ""
mainLoop = 1
while mainLoop:
    pick = input("Select a program! \n0 = quit\n1 = Hangman\n2 = Pyramid\n3 = Playfair cypher\n... ")
    if pick == "0":
        print("Goodbye ( ु⁎ᴗᵨᴗ⁎)ु.zZ")
        mainLoop = 0
    elif pick == "1":
        hangman()
    elif pick == "2":
        pyramid()
    elif pick == "3":
        playfairCypher()
    else:
        print("Please pick a valild option!")
        confusedFace()
