
import random


def triangle(T):
    if not T: return 0
    S = [ T[0][0] ]
    for i in range(1,len(T)):
        print (S)
        newS = []
        for j in range(len(T[i])):
            if j == 0: newS.append( S[0] + T[i][j] )
            elif j == len(S): newS.append( S[len(S)-1] + T[i][j] )
            else: newS.append( min(S[j-1], S[j]) + T[i][j] )
        S = newS
    print (newS)
    return min(newS)


def triangle2(T):
    if not T: return 0
    n = len(T)
    S = [0]*(n+1)
    while n >= 0:
        # There are n+1 elements on n-th row
        for i in range(0, n):
            S[i] = T[n-1][i] + min(S[i],S[i+1])
        n -= 1
    return S[0]


if __name__ == '__main__':
    T = [ [2],
          [3,4],
          [6,5,7],
          [4,1,8,3]]
    a = triangle2(T)
    print (a)