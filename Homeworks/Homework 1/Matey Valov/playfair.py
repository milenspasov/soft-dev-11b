def get_matrix(keyword):
    grid = [[0 for i in range (5)] for j in range(5)]
    keygrid = []

    for i in keyword:
        if i not in keygrid:
            if i == 'J':
                keygrid.append('I')
            else:
                keygrid.append(i)

    flag = "I" in keygrid

    for i in range(65,91):
        if chr(i) not in keygrid:
            if i == 73 and not flag:
                keygrid.append("I")
                flag = True
                
            elif i == 73 or i == 74 and flag:
                pass
            
            else:
                keygrid.append(chr(i))

    index = 0
    
    for i in range(5):
        for j in range(5):
            grid[i][j] = keygrid[index]
            index += 1

    return grid


def locate_index(char, matrix):
    index = list()

    if char == 'J':
        char = 'I'

    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if char == l:
                index.append(i)
                index.append(k)

                return index
            
def encrypt(): 
    text = input("Enter text: ").replace(" ","").upper()           

    i = 0
    for i in range(0,len(text)+1,2):
        if i < len(text) - 1:
            if text[i] == text[i+1]:
                text = text[:i+1] + 'X' + text[i+1:]

    if len(text) % 2 != 0:
        text = text[:]+'X'

    print("Encrypted text:", end = ' ')

    matrix = get_matrix(keyword)
    
    i = 0
    while i < len(text):
        n1 = list()
        n1 = locate_index(text[i], matrix)
        n2 = list()
        n2 = locate_index(text[i+1], matrix)
        
        if n1[1] == n2[1]:
            print("{}{}".format(matrix[(n1[0]+1)%5][n1[1]], matrix[(n2[0]+1)%5][n2[1]]), end = ' ')
            
        elif n1[0] == n2[0]:
            print("{}{}".format(matrix[n1[0]][(n1[1]+1)%5], matrix[n2[0]][(n2[1]+1)%5]), end = ' ')
            
        else:
            print("{}{}".format(matrix[n1[0]][n2[1]], matrix[n2[0]][n1[1]]), end = ' ')    

        i = i + 2
        
                 
def decrypt():
    text = input("\nEnter encrypted text: ").replace(" ","").upper()
    print("Decrypted message:", end = ' ')

    matrix = get_matrix(keyword)
    
    i = 0
    while i < len(text):
        n1 = list()
        n1 = locate_index(text[i], matrix)
        n2 = list()
        n2 = locate_index(text[i+1], matrix)
        
        if n1[1] == n2[1]:
            print("{}{}".format(matrix[(n1[0]-1)%5][n1[1]], matrix[(n2[0]-1)%5][n2[1]]), end = ' ')
            
        elif n1[0] == n2[0]:
            print("{}{}".format(matrix[n1[0]][(n1[1]-1)%5], matrix[n2[0]][(n2[1]-1)%5]),end = ' ')
            
        else:
            print("{}{}".format(matrix[n1[0]][n2[1]], matrix[n2[0]][n1[1]]), end = ' ')    

        i = i + 2        

keyword = "TUES"
encrypt()
decrypt()
