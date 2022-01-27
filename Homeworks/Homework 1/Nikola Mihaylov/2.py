from random import randint

size = 4
triangle = [[randint(0, 9) for _ in range(0, i)] for i in range(1, size + 1)]

def sum_(l, x, y):
    if x + 1 == size:
        return l[x][y]
    left = right = l[x][y]
    left += sum_(l, x + 1, y)
    right += sum_(l, x + 1, y + 1)
    return max(left, right)

for l in triangle:
    for i in l:
        print(i, end = ' ')
    print()
print(sum_(triangle, 0, 0))
