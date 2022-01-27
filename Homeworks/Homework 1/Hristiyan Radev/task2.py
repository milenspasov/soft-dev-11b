import random

list_of_numbers = []
list_of_row_numbers = []
list_of_rows = []

for num in range(5050): # Сложил съм 5050, защото толкова е броя на числата ако искам редовете да са 100
    list_of_numbers.append(random.randint(0,101))

row = to_be_print = 1

for number in list_of_numbers:
    list_of_row_numbers.append(number)
    if row == to_be_print:
        list_of_rows.append(list_of_row_numbers)
        list_of_row_numbers = []
        row += 1
        to_be_print = 0

    to_be_print += 1

row = len(list_of_rows) - 1

for row in range(row - 1, -1, -1):
    for column in range(row + 1):

        if list_of_rows[row+1][column] > list_of_rows[row+1][column+1]:
            list_of_rows[row][column] += list_of_rows[row+1][column]
        else:
            list_of_rows[row][column] += list_of_rows[row+1][column+1]

print(list_of_rows[0][0])
