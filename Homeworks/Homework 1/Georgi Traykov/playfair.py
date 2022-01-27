from textwrap import wrap

def decrypt_syllables(matrix, index, syllable):
    r1 = 0
    r2 = 0
    c1 = 0
    c2 = 0
    syllable_cp = syllable[index]
    decrypted_input = ""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == syllable_cp[0]:
                r1 = i
                c1 = j
            if matrix[i][j] == syllable_cp[1]:
                r2 = i
                c2 = j
            if r1 == r2:
                if c2 == 0:
                    decrypted_input = matrix[r1][c1-1] + matrix[r2][4]
                else:
                    decrypted_input = matrix[r1][c1-1] + matrix[r2][c2-1]
            if c1 == c2:
                if r2 == 0:
                    decrypted_input = matrix[r1-1][c1] + matrix[4][c2]
                else:
                    decrypted_input = matrix[r1-1][c1] + matrix[r2-1][c2]
            if r1 != r2 and c1 != c2:
                    decrypted_input = matrix[r1][c2] + matrix[r2][c1]
    
    return decrypted_input

def encrypt_syllables(matrix, index, syllable):
    r1 = 0
    r2 = 0
    c1 = 0
    c2 = 0
    syllable_cp = syllable[index]
    encrypted_input = ""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == syllable_cp[0]:
                r1 = i
                c1 = j
            if matrix[i][j] == syllable_cp[1]:
                r2 = i
                c2 = j
            if r1 == r2:
                if c2 == 4:
                    encrypted_input = matrix[r1][c1+1] + matrix[r2][0]
                else:
                    encrypted_input = matrix[r1][c1+1] + matrix[r2][c2+1]
            if c1 == c2:
                if r2 == 4:
                    encrypted_input = matrix[r1+1][c1] + matrix[0][c2]
                else:
                    encrypted_input = matrix[r1+1][c1] + matrix[r2+1][c2]
            if r1 != r2 and c1 != c2:
                    encrypted_input = matrix[r1][c2] + matrix[r2][c1]
    
    return encrypted_input

matrix = [
    ["T","U","E","S","A"],
    ["B","C","D","F","G"],
    ["H","I","K","L","M"],
    ["N","O","P","Q","R"],
    ["V","W","X","Y","Z"]
]


print("Keyword: TUES\n")
print("Playfair Matrix")
print("---------------")

for i in range(5):
    for j in range(5):
        print(matrix[i][j], " ", end = '')
    print()

while(1):
    option = int(input("Do you want to decrypt or encrypt text(1/2):"))

    if option == 1:
        phrase = input("Enter the text you want to decrypt:")
        phrase = phrase.replace(" ", "")
        phrase = phrase.upper()
        syllable_phrase = wrap(phrase, 2)

        print("Decrypted text:", end='')
        for i in range(len(syllable_phrase)):
            print(decrypt_syllables(matrix, i, syllable_phrase), " ", end='')
        break

    if option == 2:
        phrase = input("Enter the text you want to encrypt: ")
        phrase = phrase.replace(" ", "")
        for i in range(len(phrase)):
            if i < len(phrase)-1:
                if phrase[i] == phrase[i+1]:
                    phrase = phrase[:i+1] + "x" + phrase[i+1:]
        if(len(phrase) % 2) != 0:
            phrase = phrase + "x"
        phrase = phrase.upper()

        syllable_phrase = wrap(phrase, 2)

        print("Encrypted text:", end='')
        for i in range(len(syllable_phrase)):
            print(encrypt_syllables(matrix, i, syllable_phrase), " ", end='')
        break
    else:
        print("Enter 1 for decryption and 2 for encryption.")


