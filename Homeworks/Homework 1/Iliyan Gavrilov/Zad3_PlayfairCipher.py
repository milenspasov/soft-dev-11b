# creates matrix from keyword
def createKeyMatrix(matrix, keyword):
    #append key into array
    Key = list()
    for i in keyword:
        if(i not in Key): # check for repeating letters
            if i == 'J':
                Key.append('I')
            else:
                Key.append(i)

    #append rest of alphabet into array except J (J = I)
    for i in range(ord('A'), ord('J')):
        if chr(i) not in Key: # check for repeating letters
            Key.append(chr(i))      
    for i in range(ord('K'), ord('Z')+1):
        if chr(i) not in Key: # check for repeating letters
            Key.append(chr(i))

    #put array into matrix       
    index = 0 
    for i in range(5): 
        for j in range(5):
            matrix[i][j] = Key[index]
            index+=1

# split the message into pairs of letters
def convertPairsOfMessage(message):
    for i in range(0,len(message)+1,2):
        if(i < len(message) - 1):
            if(message[i] == message[i+1]):
                message = message[:i+1] + "X" + message[i+1:] # add "X" if there are 2 of the same letter in one pair 

    if(len(message) % 2 != 0): # add "X" if there are an odd amount of letters
        message = message + "X"
    
    return message

#search for letters in matrix
def search(matrix, a, b):
    coords = list()
    for i in range(5): # search for letters in the matrix
        for j in range(5):
            if(matrix[i][j] == a):
                coords.insert(0, i)
                coords.insert(1, j)
            if(matrix[i][j] == b):
                coords.insert(2, i)
                coords.insert(3, j)
    return coords

# encrypts the message       
def encrypt(matrix, a, b): 
    coords = list() # search for coordinates of the pair of letters
    if(a == 'J'):
        a = 'I'
    elif( b == 'J'):
        b = 'I'
    
    coords = search(matrix, a, b)        
    # check how the letters are positioned relative to each other and find which of the cases they're in
    if(coords[1] == coords[3]): # same column case
        if(coords[0]+1 >= 5):
            coords[0] = -1
        if(coords[2]+1 >= 5):
            coords[2] = -1
        a = matrix[coords[0]+1][coords[1]]
        b = matrix[coords[2]+1][coords[3]]
    elif(coords[0] == coords[2]): # same row case
        if(coords[1]+1 >= 5):
            coords[1] = -1
        if(coords[3]+1 >= 5):
            coords[3] = -1
        a = matrix[coords[0]][coords[1]+1]
        b = matrix[coords[2]][coords[3]+1]
    else: # rectangle case
        a = matrix[coords[0]][coords[3]]
        b = matrix[coords[2]][coords[1]]

    print(a + b, end = ' ')

# decrypts the message
def decrypt(matrix, a, b): 
    coords = list() # search for coordinates of the pair of letters
    if(a == 'J'):
        a = 'I'
    elif( b == 'J'):
        b = 'I'
        
    coords = search(matrix, a, b)
    # check how the letters are positioned relative to each other and find which of the cases they're in
    if(coords[1] == coords[3]): # same column case
        a = matrix[coords[0]-1][coords[1]]
        b = matrix[coords[2]-1][coords[3]]
    elif(coords[0] == coords[2]): # same row case
        a = matrix[coords[0]][coords[1]-1]
        b = matrix[coords[2]][coords[3]-1]
    else: # rectangle case
        a = matrix[coords[0]][coords[3]]
        b = matrix[coords[2]][coords[1]]
    
    print(a + b, end = '')
    if(a == 'I' or b == 'J'):
        if(a == 'I'):
            a = 'J'
        elif( b == 'I'):
            b = 'J'
    return a, b

# define Polybius square, keyword and message to be encrypted
matrix = [["" for i in range(5)] for j in range(5)]
keyword = "TUES"
print("Encrypt or decrypt a message: ", end = '')
encrypt_or_decrypt = input()
print("Keyword: " + keyword)
print("Message: ", end = '')
message = input()
print()

# turn lower case letters into upper case letters
keyword = keyword.upper()
message = message.upper()

# remove all spaces from strings
keyword = keyword.replace(" ", "")
message = message.replace(" ", "")

#print(keyword,  message, "\n")
createKeyMatrix(matrix, keyword)

message = convertPairsOfMessage(message) # change the individual pairs of the message (double letters, odd number of letters)

# encrypt the message in a loop
if(encrypt_or_decrypt == "encrypt"):
    print("Encryption:")
    for i in range(0,len(message),2):
        if(i < len(message) - 1):
            encrypt(matrix, message[i], message[i+1])
elif(encrypt_or_decrypt == "decrypt"):
    word_with_j = list()
    print("Decryption:")
    for i in range(0,len(message),2):
        if(i < len(message) - 1):
            word_with_j.append(decrypt(matrix, message[i], message[i+1]))
    print(" or ", end = '')
    for i in range(len(word_with_j)):
        print(word_with_j[i][0], end = '')
        print(word_with_j[i][1], end = '')
else:
    print("'" + encrypt_or_decrypt + "' is not valid! Choose either 'encrypt' or 'decrypt'")
