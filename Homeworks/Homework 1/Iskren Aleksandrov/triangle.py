# 2. Сметнете най-голямата сума от върха на триъгълника до основата. От всеки елемент може да се придвижите до двата под него (в ляво и дясно) или двата над него.
#
# Пример:
#       3
#     7 4
#   2 4 6
# 8 5 9 3
#
# Най-голямата сума е на пътя 3-7-4-9 или общо 23.
# Решете задачата с триъгълник от 100 реда като първо генерирате числата случайно.

from random import randrange

MAX_NUM = 6
ROWS = 5

nodes = []
def init_triangle():
    for i in range(ROWS):
        curr = []
        for n in range(i+1):
            curr.append(randrange(MAX_NUM))
        nodes.append(curr)

def solve_triangle():
    for i in range(ROWS-2, -1, -1):
        # 3
        for k in range(len(nodes[i])):
            # nodes[i] = [2, 5, 0]
            nodes[i][k] += max(nodes[i+1][k], nodes[i+1][k+1])

def print_triangle():
    for node in nodes:
        for value in node:
            print(value, end=' ')
        print()

init_triangle()

print("Generated Triangle:")
print_triangle()

solve_triangle()

print("\nSolved Triangle:")
print_triangle()

print("\nSolution:", nodes[0][0])