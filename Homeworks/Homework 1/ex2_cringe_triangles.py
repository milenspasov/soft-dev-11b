import random
#import math

rows = 100
tab = rows - 1
#num_list = []
#row_num = []
#row_list = []

#Създаване на матрицата
matrix = [[0 for i in range(rows)]for j in range(rows)]

for i in range(rows):
    for j in range(tab):
        print(end= " ")
    tab -= 1

    #Въвеждане на случайните числа
    for j in range(i+1):
        matrix[i][j] = random.randint(0,9)
        print(matrix[i][j], "", end= "")
    print("\n")

m = rows - 1
#sum = 0

for i in range(m-1, -1, -1):
    for j in range(i+1):
        #Намиране на по-голямото от двете числа
        if(matrix[i+1][j] > matrix[i+1][j+1]):
            matrix[i][j] += matrix[i+1][j]

        else:
            matrix[i][j] += matrix[i+1][j+1]

print("The largest sum is", matrix[0][0])