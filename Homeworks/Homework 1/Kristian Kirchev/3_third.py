shifur = [['T', 'U', 'E', 'S', 'A'],
          ['B', 'C', 'D', 'F', 'G'],
          ['H', 'I', 'K', 'L', 'M'],
          ['N', 'O', 'P', 'Q', 'R'],
          ['V', 'W', 'X', 'Y', 'Z']]


def find(l1, l2, shifur):
    coords = [[], []]

    for i in range(0, 5):
        for j in range(0, 5):
            if(shifur[i][j] == l1):
                coords[0] = [i, j]

            if(shifur[i][j] == l2):
                coords[1] = [i, j]

    return coords


def col(pair):
    word = ""

    if(pair[1][1]+1 == 5):
        pair[1][1] = -1
    if(pair[0][1]+1 == 5):
        pair[0][1] = -1

    word += shifur[pair[0][0]][pair[0][1]+1]
    word += shifur[pair[1][0]][pair[1][1]+1]
    word += ' '

    return word


def row(pair):
    word = ""

    if(pair[1][0]+1 == 5):
        pair[1][0] = -1
    if(pair[0][0]+1 == 5):
        pair[0][0] = -1

    word += shifur[pair[0][0]+1][pair[0][1]]
    word += shifur[pair[1][0]+1][pair[1][1]]
    word += ' '

    return word


def box(pair):
    word = ""
    word += shifur[pair[0][0]][pair[1][1]]
    word += shifur[pair[1][0]][pair[0][1]]
    word += ' '

    return word


def encrypt(word, shifur):
    encrypt = ""

    for i in range(0, int(len(parsed)/2)):
        pair = find(word[i*2], word[i*2+1], shifur)

        if(pair[0][0] == pair[1][0]):
            encrypt += col(pair)

        elif(pair[0][1] == pair[1][1]):
            encrypt += row(pair)

        else:
            encrypt += box(pair)

    return encrypt


def re_colomn(pair):
    word = ""

    if(pair[1][1]-1 == -1):
        pair[1][1] = 4
    if(pair[0][1]-1 == -1):
        pair[0][1] = 4

    word += shifur[pair[0][0]][pair[0][1]-1]
    word += shifur[pair[1][0]][pair[1][1]-1]
    word += ' '

    return word


def re_row(pair):
    word = ""

    if(pair[1][0]-1 == -1):
        pair[1][0] = 4
    if(pair[0][0]-1 == -1):
        pair[0][0] = 4

    word += shifur[pair[0][0]-1][pair[0][1]]
    word += shifur[pair[1][0]-1][pair[1][1]]
    word += ' '

    return word


def decrypt(word, shifur):
    decrypt = ""

    for i in range(0, int(len(parsed)/2)):
        pair = find(word[i*2], word[i*2+1], shifur)

        if(pair[0][0] == pair[1][0]):
            decrypt += re_colomn(pair)

        elif(pair[0][1] == pair[1][1]):
            decrypt += re_row(pair)

        else:
            decrypt += box(pair)

    return decrypt


mode = int(input("Choose mode(decrypt[0]/encrypt[1]):"))

word = str(input("Choose word to check: "))
word = word.upper()

for i in range(0, len(word)):
    if(word[i] == 'J'):
        word = list(word)
        word[i] = 'I'

parsed = [word[0]]

for i in range(1, len(word)):
    if(word[i] == ' '):
        continue
    if(word[i-1] == word[i]):
        parsed.append('X')

    parsed.append(word[i])

if(len(word) % 2 == 1):
    parsed.append('X')

if(mode):
    print(encrypt(parsed, shifur))
else:
    print(decrypt(parsed, shifur))
