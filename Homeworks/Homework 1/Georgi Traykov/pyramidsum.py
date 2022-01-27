import random

while 1:
    rows = input("Enter number of rows:")
    rows = int(rows)
    if 1 <= rows <= 100:
        break
    else:
        print("Enter a whole number between 1 and 100!")

rows_minusone = rows - 1
cols_minusone = rows - 1
total = rows

for i in range(1, rows, 1):
    total += rows-i

 
pyramid = [[0 for c in range(rows)] for r in range(rows)]

for i in range(rows):
    print(' ' * (rows_minusone-i), end='')
    for j in range(i+1):
            pyramid[i][j] = random.randint(1, 9)
            print(pyramid[i][j], end=" ")
    print()

#for r in pyramid:
    #for c in r:
        #print(c, end=" ")
    #print()


def maxPathSum(pyramid, rows_minusone, cols_minusone):# 2 2
 #smetka otdolu nagore
    for i in range(rows_minusone-1, -1, -1):# 1 0
        for j in range(i+1):# 0 1 0
            if (pyramid[i+1][j] > pyramid[i+1][j+1]):
                pyramid[i][j] += pyramid[i+1][j]
            else:
                pyramid[i][j] += pyramid[i+1][j+1]

    return pyramid[0][0]


print("The max path sum of the", rows, "row pyramid is", maxPathSum(pyramid, rows_minusone, cols_minusone), ".")#m = n = broi redove/koloni v pyramidta
 