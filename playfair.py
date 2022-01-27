
keyword = "TUES"

cipher = [['T', 'U', 'E', 'S', 'A'],
['B', 'C', 'D', 'F', 'G'],
['H', 'I', 'K', 'L', 'M'],
['N', 'O', 'P', 'Q', 'R'],
['V', 'W', 'X', 'Y', 'Z']]

word = input("type a word: ")

arrx = ["X"]
arrchar = []

letter = 0
while letter < len(word): #puts the input word into pairs
    if letter+1 == len(word):
        break
    if word[letter] == "J":
        word[letter] = "I"
    elif word[letter+1] == "J":
        word[letter+1] = "I"
    if not(word[letter] == word[letter+1]):
        arrchar.append(word[letter] + word[letter+1])
        letter = letter + 2
    
    else:
        arrchar.append(word[letter] + arrx[0])
        if (letter + 1) == (len(word)-1):
            arrchar.append(word[letter+1] + arrx[0])
        letter = letter + 1 
    if letter == (len(word)-1):
            arrchar.append(word[letter] + arrx[0])

count = 0

while count < len(arrchar):
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    i = 0
    j = 0
    arrl = []
    while i < 5:
        for f in arrchar[count]:
            arrl.append(f)
        while j < 5:
            
            if str(arrl[0]) == str(cipher[i][j]):
                x = i
                y = j
            elif str(arrl[1]) == str(cipher[i][j]):
                x1 = i
                y1 = j
            j = j + 1
        j = 0
        i = i + 1
      
    arr2 = []

    if x == x1:
        if y == 4:
            arr2.append(cipher[x][0])
        else:
            arr2.append(cipher[x][y+1])
            
        if y1 == 4:
            arr2.append(cipher[x1][0])
        else:
            arr2.append(cipher[x1][y1+1])
    elif y == y1:
        if x == 4:
            arr2.append(cipher[0][y])
        else:
            arr2.append(cipher[x+1][y])
        if x1 == 4:
            arr2.append(cipher[0][y1])
        else:
            arr2.append(cipher[x1+1][0])
    else:
        arr2.append(cipher[x][y1])
        arr2.append(cipher[x1][y])

    print(arr2[0])
    print(arr2[1])
    count = count + 1
              

