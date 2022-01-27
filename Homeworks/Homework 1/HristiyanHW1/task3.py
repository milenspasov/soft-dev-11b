import re

word = "TUES"
indexes_for_X = [] #Лист, в който слагам на кои индекси трябва да сложа Х
message = "HOPEFULLY TO GRADUATE"
message = message.replace(' ', '')
message = message.upper()
matrix = [[0 for x in range(5)] for y in range(5)]
letters = [] #Тук слагам буквите, които се срещат само единично, за да мога после да ги сложа в матрицата
flag = 0

for index in range(1, len(message), 2):
    if message[index] == message[index - 1]:
           indexes_for_X.append(index)
           

string_as_list = list(message.strip(" ")) #Правя стринга на лист, за да мога по лесно да сложа между буквите, които трябва, Х

count = 0 #Този брояч ми помага да знам с колко знака се отмества мястото, където трябва да сложа Х
#Например ако трябва да сложа Х на идекс 3, но преди това съм сложил на индекс 1, ако нямам този брояч думата ще изглежда така - 
#TXTXSS, а трябва да е TXTSXS

for index in indexes_for_X:
    string_as_list.insert(index + count, "X")
    count += 1
message = "".join(string_as_list)
    
if len(message) % 2 == 1:
    message += "X"

for character in word:
    if character not in letters:
        if character == 'J':
            letters.append("I")
        else:
            letters.append(character)
            
for character in range(65, 91):
    if chr(character) not in letters:
        if chr(character) == "J" and "I" not in letters:
            letters.append("I")
            flag=1
        elif flag==0 and character == 73 or character == 74:
                pass    
        else:
            letters.append(chr(character))
order_count = 0

for row in range(5):
    for column in range(5):
        matrix[row][column] = letters[order_count]
        order_count += 1
        
pairs_of_message = re.findall('..', message)

first_X = first_Y = second_X = second_Y = 0
crypted_word = ''

for pair in pairs_of_message:
    for row in range(5):
        for column in range(5):
            if matrix[row][column] == pair[0]:
               first_X = row;
               first_Y = column
            elif matrix[row][column] == pair[1]:
               second_X = row;
               second_Y = column
       
    if first_X == second_X:
            if first_Y + 1 > 4:
               crypted_word += matrix[first_X][0]
               crypted_word += matrix[second_X][second_Y + 1]
            elif second_Y + 1 > 4:
                crypted_word += matrix[first_X][first_Y + 1]
                crypted_word += matrix[second_X][0]
            else:
               crypted_word += matrix[first_X][first_Y + 1]
               crypted_word += matrix[second_X][second_Y + 1]
    elif first_Y == second_Y:
        if first_X + 1 > 4:
            crypted_word += matrix[0][first_Y]
            crypted_word += matrix[second_X + 1][second_Y]
        elif second_X + 1 > 4:
            crypted_word += matrix[first_X + 1][first_Y]
            crypted_word += matrix[0][second_Y]
        else:
            crypted_word += matrix[first_X + 1][first_Y]
            crypted_word += matrix[second_X + 1][second_Y]
    else:
        crypted_word += matrix[first_X][second_Y]
        crypted_word += matrix[second_X][first_Y]

print(crypted_word)