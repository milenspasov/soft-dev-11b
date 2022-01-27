import random
from random import randint

rows = 100 # Define number of rows in triangle

''' Start from the buttom and sum the bigger number until the top element
    is reached and the top element will contain the sum so the function returns it'''
def Find_Max_Sum(triangle):
    for i in range(rows-2, -1, -1):
        for j in range(i+1):
            if(triangle[i+1][j] > triangle[i+1][j+1]):
                triangle[i][j] +=  triangle[i+1][j]
            else:
                triangle[i][j] += triangle[i+1][j+1]
    return triangle[0][0]


triangle = [[0 for i in range(rows)] for j in range(rows)]

# Fills the triangle with random values

for i in range(rows):
    for j in range(i+1):
        triangle[i][j] = random.randint(0, 100) # number range

    
# Fills the triangle with random values AND ALSO PRINTS IT!
'''
print("INPUT:")
for i in range(rows):
    for l in range(rows - i):
        print(" ", end = '');
    for j in range(i+1):
        print(triangle[i][j], end = ' ')
    print()
print()
'''

print("MAX SUM =", Find_Max_Sum(triangle)) # calls the function to find the biggest sum and prints it
