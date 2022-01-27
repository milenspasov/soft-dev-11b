import random 
import numpy as np

matr = np.zeros( (100, 100) )

for m in range(100):
    for m2 in range(m):
        matr[m][chis = random.randint(0, 100) for chis in range(m2)]

# Function for finding maximum sum
def maxPathSum(tri, m, n):
        
    for i in range( m - 1, -1, -1 ):
        for j in range(i + 1):

            if (tri[i + 1][j] > tri[i + 1][j + 1]):
                tri[i][j] += tri[i + 1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]
 
    return tri[0][0]
 """
tri = [ [random.randint(0, 100), 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), 0, 0, 0, 0, 0, 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
      0, 0, 0, 0, 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100), 0, 0, 0, 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100),random.randint(0, 100), 0, 0, 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100),random.randint(0, 100), random.randint(0, 100),
       0, 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100),random.randint(0, 100), random.randint(0, 100),
       random.randint(0, 100), 0, 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100),random.randint(0, 100), random.randint(0, 100),
       random.randint(0, 100), random.randint(0, 100), 0, 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100),random.randint(0, 100), random.randint(0, 100),
       random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 0],
       [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
       random.randint(0, 100),random.randint(0, 100), random.randint(0, 100),
       random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
       random.randint(0, 100)]]"""

print(maxPathSum(matr, 2, 2))
