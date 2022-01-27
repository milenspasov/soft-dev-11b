import random
import math

keyword = "TUES"
keyword = keyword.upper()
matrix = [[0 for i in range (5)] for j in range(5)]
letters = []
m = 0
n = 0
index = 0

#Добавяне на ключовата дума в матирацата
for letter in keyword:
    if letter not in letters:
        matrix[m][n] = letter
        letters.append(letter)
    else:
        continue
    if (n==4):
        n = 0
        m += 1
    else:
        n += 1

for letter in range(65,91):
    if letter==74:
            continue

    #Да не се добавят повтарящи се букви
    if chr(letter) not in letters:
        letters.append(chr(letter))

for i in range(5):
    for j in range(5):
        matrix[i][j] = letters[index]
        index+=1

def separate_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + "X"
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=2   
    return message

#Връща индекс, който ще е нужен за употребата на правила 1-4
def index_find(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue


def playfair(message):
    inc = -1
    message = message.upper()
    message = message.replace(" ","")    
    message = separate_letters(message)
    cipher_text=''

    for (l1, l2) in zip(message[0::2], message[1::2]):
        m1,n1 = index_find(l1,matrix)
        m2,n2 = index_find(l2,matrix)

        #Правило 2
        if m1==m2:
            cipher_text += matrix[m1][(n1+inc)%5] + matrix[m2][(n2+inc)%5]

        #Правило 3
        elif n1==n2:
            cipher_text += matrix[(m1+inc)%5][n1] + matrix[(m2+inc)%5][n2]

        #Правило 4
        else:
            cipher_text += matrix[m1][n2] + matrix[m2][n1]
    
    return cipher_text

if __name__=="__main__":
    print ("Decrypting")
    print ( playfair("ABCDFGHIKLMNOPQRVWXYZ"))
