from textwrap import wrap

table = [
    ['T', 'U', 'E', 'S', 'A'],
    ['B', 'C', 'D', 'F', 'G'],
    ['H', 'I/J', 'K', 'L', 'M'],
    ['N', 'O', 'P', 'Q', 'R'],
    ['V', 'W', 'X', 'Y', 'Z']
]

word = input()
word = word.upper()
splitted_word = word

while True:
    flag = 0
    splitted_word = wrap(splitted_word, 2)

    for index, value in enumerate(splitted_word):
        splitted_word[index] = list(value)

        if len(splitted_word[index]) == 2:
            if splitted_word[index][0] == splitted_word[index][1]:
                splitted_word[index].append(splitted_word[index][1])
                splitted_word[index][1] = 'X'
                flag = 1
        splitted_word[index] = ''.join(splitted_word[index])
    splitted_word = ''.join(splitted_word)

    if flag == 0:
        break

if len(splitted_word) % 2 == 1:
    splitted_word += 'X'

splitted_word = wrap(splitted_word, 2)
for p_index, pair in enumerate(splitted_word):
    row_index_1 = None
    col_index_1 = None
    row_index_2 = None
    col_index_2 = None
    for l_index, letter in enumerate(pair):
        for r_index, row in enumerate(table):
            for v_index, value in enumerate(row):
                if letter in value:
                    if l_index == 0:
                        col_index_1 = v_index
                        row_index_1 = r_index
                    else:
                        col_index_2 = v_index
                        row_index_2 = r_index

    pair = list(pair)
    if col_index_1 == col_index_2:
        if row_index_1 + 1 == 5:
            row_index_1 = 0
        else:
            row_index_1 += 1 

        if row_index_2 + 1 == 5:
            row_index_2 = 0
        else:
            row_index_2 += 1
    elif row_index_1 == row_index_2:
        if col_index_1 + 1 == 5:
            col_index_1 = 0
        else:
            col_index_1 += 1

        if col_index_2 + 1 == 5:
            col_index_2 = 0
        else:
            col_index_2 += 1
    else:
        temp = col_index_1
        col_index_1 = col_index_2
        col_index_2 = temp

    pair[0] = table[row_index_1][col_index_1]
    pair[1] = table[row_index_2][col_index_2]

    pair = ''.join(pair)
    splitted_word[p_index] = pair


splitted_word = ''.join(splitted_word)
print(splitted_word)