#pravi matricata kato list
def make_matrix_as_list(word):
    abcs=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key="TUES"
    matrix_as_list=[]
    matrix=[]
    for i in key:
        if i in abcs:
            abcs.remove(i)
            matrix_as_list.append(i)
    for i in abcs:
        matrix_as_list.append(i)
    return matrix_as_list
#dumata na dvoiki
def make_word_as_pairs(word):
    word_as_list=[]
    for i in word:
        if i!=' ':
            word_as_list.append(i.upper())

    for i in range(len(word_as_list)-1):
        if word_as_list[i]==word_as_list[i+1]:
            word_as_list.insert(i+1,'X')
    if len(word_as_list)%2==1:
        word_as_list.append('X')
    word_as_pairs=[]
    for i in range(int(len(word_as_list)/2)):
        word_as_pairs.append(word_as_list[i*2:(i+1)*2])
    return word_as_pairs

#dumata ot dvoiki bukvi pravi na dvoiki indexi
def to_num_pairs(word_as_pairs):
    new_word_as_num_pairs=[]
    for i in word_as_pairs:
        pair=[]
        for j in i:
            for k in range(len(matrix_as_list)):
                if matrix_as_list[k]==j:
                    pair.append(k)
        new_word_as_num_pairs.append(pair)
    return new_word_as_num_pairs

#ot syobshtenie index do encripted index
def pair_to_pair(old_pair):
    x=old_pair[0]
    y=old_pair[1]
    #na edin red
    if x-(x%5)==y-(y%5):
        return [  (x-x%5)+(x+1)%5  ,(y-y%5)+(y+1)%5]
    #edna kolona
    if x%5==y%5:
        return [(x+5)%25,(y+5)%25]
    #kvadrat
    return [
        x-(x%5-y%5)
        ,
        y+(x%5-y%5)
    ]
print("key:")
matrix_as_list=make_matrix_as_list(input())
print("word:")
word_as_pairs=make_word_as_pairs(input())
word_as_num_pairs=to_num_pairs(word_as_pairs)
new_word_as_num_pairs=[]
for i in word_as_num_pairs:
    new_word_as_num_pairs.append(pair_to_pair(i))

for i in new_word_as_num_pairs:
    for j in i:
        print(matrix_as_list[j],end='')
