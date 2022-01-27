import random
lines = 100
spaces = lines - 1

matrix = [[0 for i in range(lines)]for j in range(lines)]

for i in range(lines):
    for k in range(spaces):
        print(end = " ")

    spaces -= 1;

    for j in range(i+1):
        matrix[i][j] = random.randint(1,9)
        print(matrix[i][j], "", end = "")

    print("\r")

m = lines - 1

for i in range(m-1, -1, -1):
    for j in range(i+1):

        if(matrix[i+1][j] > matrix[i+1][j+1]):
            matrix[i][j] += matrix[i+1][j]

        else:
            matrix[i][j] += matrix[i+1][j+1]

print("Largest sum of path is", matrix[0][0])
