import string

KEYPHRASE = "TUES"
alphabet = string.ascii_lowercase.upper()

matrix = []

def prep_msg(msg):
    if((len(msg) % 2) != 0):
        msg += 'X'
    result = ''

    counter = 1
    for letter in msg:
        if(letter == ' '):
            continue
        if (counter == 1):
            temp = letter
            counter = 2
        else:
            if(letter != temp):
                temp += letter
            else:
                temp += 'X ' + letter
                continue
            result += temp.upper() + " "
            counter = 1
    return result

def init_matrix():
    temp = []
    for letter in KEYPHRASE:
        temp.append(letter)
    matrix.append(temp)

    i = 0
    k = len(KEYPHRASE)
    for letter in alphabet:
        if(letter == 'J'):
            continue
        if(k == 5):
            matrix.append([])
            i += 1
            k = 0
        if(letter not in KEYPHRASE):
            matrix[i].append(letter)
            k += 1

# function to use the matrix to encrypt plaintext into playfair cipher
def encrypt(msg):
    msg = prep_msg(msg).split(" ")
    print(msg)
    result = ''
    for letter in msg:
        if(letter == ' ' or letter == ''):
            continue
        row = 0
        col = 0
        for i in range(len(matrix)):
            if(letter[0] in matrix[i]):
                row = i
                col = matrix[i].index(letter[0])
            
        row2 = 0
        col2 = 0
        for i in range(len(matrix)):
            if(letter[1] in matrix[i]):
                row2 = i
                col2 = matrix[i].index(letter[1])

        if(row == row2):
            if(col == 4):
                result += matrix[row][0] + matrix[row2][col2+1] + " "
            if(col2 == 4):
                result += matrix[row][col+1] + matrix[row2][0] + " "
            else:
                result += matrix[row][col+1] + matrix[row2][col2+1] + " "
        elif(col == col2):
            if(row == 4):
                result += matrix[0][col] + matrix[row2+1][col2] + " "
            if(row2 == 4):
                result += matrix[row+1][col] + matrix[0][col2] + " "
            else:
                result += matrix[row+1][col] + matrix[row2+1][col2] + " "
        else:
            print(col, row, col2, row2)
            result += matrix[row][col2] + matrix[row2][col] + " "
                
    #     if((col + 1) == 5):
    #         result += matrix[row][0]
    #     else:
    #         result += matrix[row][col + 1]
    return result

msg = input("Message to decode: ")

init_matrix()

print(matrix)

print(encrypt(msg))