import random

arr=[]
n=100
for i in range(n):
    row = []
    for j in range(i+1):
        row.append(random.randint(0,100))
    arr.append(row)

x,y=(0,0)
res=arr[y][x]
for i in range(n-1):
    res+=max(arr[y+1][x], arr[y+1][x+1])
    x = x if (arr[y+1][x] > arr[y+1][x+1]) else (x+1)
    y+=1

print(res)

