import random


def do(tree):
    for i in range(len(tree)):
        for j in range(len(tree[i])):
            if i>0:
                one = tree[i-1][j-1]+tree[i][j]
                two=0
                if j<len(tree[i])-1:
                    two = tree[i-1][j]+tree[i][j]
                if(one>two):
                    tree[i][j]=one
                else:
                    tree[i][j]=two
    print(max(tree[len(tree)-1]))
    
tree=[]
for i in range(100):
    tree.append([])
    for j in range(i+1):
        tree[i].append(random.randint(0,100))
do(tree)

