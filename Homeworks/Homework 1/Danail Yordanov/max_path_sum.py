from random import randint

tree = list()
path_sum = 0

for i in range(1, 101):
    row = list()
    for j in range(1, (i + 1)):
        row.append(randint(1, 9))
    tree.append(row)

bigger_index = None

if tree[1][0] > tree[1][1]:
    bigger_index = 0
elif tree[1][0] < tree[1][1]:
    bigger_index = 1
else:
    bigger_index = 0

path_sum += tree[0][0]
path_sum += tree[1][bigger_index]

for i in range(0, 100):
    print(tree[i])

for i in range (2, 100):
    if tree[i][bigger_index + 1] > tree[i][bigger_index]:
        path_sum += tree[i][bigger_index + 1]
        bigger_index = bigger_index + 1
    else:
        path_sum += tree[i][bigger_index]

print(path_sum)