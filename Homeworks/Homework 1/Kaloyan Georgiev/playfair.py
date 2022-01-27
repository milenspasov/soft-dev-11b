from math import fmod
CIPHER_WIDTH = 5
CIPHER_HEIGHT = 5
cipher = [
    "T", "U", "E", "S", "A",
    "B", "C", "D", "F", "G",
    "H", "I", "K", "L", "M",
    "N", "O", "P", "Q", "R",
    "V", "W", "X", "Y", "Z"
]

def encrypt(message):
    midmessage = message.upper().replace(" ", "")
    encrypted = ""
    if(len(midmessage) % 2 == 1):
        midmessage += "X"
    midmessage = midmessage.replace("J", "I")
    #print(midmessage)
    for i in range(0, len(midmessage), 2):
        #print(i)
        index1 = cipher.index(midmessage[i])
        #print("index 1 {0} = {1}".format(index1, cipher[index1]))
        index2 = cipher.index(midmessage[i+1])
        #print("index 2 {0} = {1}".format(index2, cipher[index2]))
        #Column case
        if(index1 % CIPHER_WIDTH == index2 % CIPHER_WIDTH):
            #print("column case")
            encrypted += cipher[index1+CIPHER_WIDTH] if (index1+CIPHER_WIDTH) // CIPHER_WIDTH < CIPHER_HEIGHT else cipher[index1 % CIPHER_WIDTH]
            encrypted += cipher[index2+CIPHER_WIDTH] if (index2+CIPHER_WIDTH) // CIPHER_WIDTH  < CIPHER_HEIGHT else cipher[index2 % CIPHER_WIDTH]

        #Row case
        elif(index1 // CIPHER_WIDTH  == index2 // CIPHER_WIDTH):
            #print("row case")
            encrypted += cipher[index1+1] if ((index1+1) % CIPHER_WIDTH > index1 % CIPHER_WIDTH) else cipher[index1 - (index1 % CIPHER_WIDTH)]
            encrypted += cipher[index2+1] if ((index2+1) % CIPHER_WIDTH > index2 % CIPHER_WIDTH) else cipher[index2 - (index2 % CIPHER_WIDTH)]
            #print(encrypted[-2:])
        #Rectangle case
        else:
            #print("rect case")
            if(index2 % 5 < index1 % 5):
                encrypted += cipher[index1 - (index1 % 5 - index2 % 5)]
                encrypted += cipher[index2 + (index1 % 5 - index2 % 5)]
            else:
                encrypted += cipher[index1 + (index2 % 5 - index1 % 5)]
                encrypted += cipher[index2 - (index2 % 5 - index1 % 5)]

        encrypted += " "
    return encrypted
string = input("Enter word to encrypt: ")
print(encrypt(string))