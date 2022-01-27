
k = [
    "T",	"U",	"E",	"S",	"A",
    "B",	"C",	"D",	"F",	"G",
    "H",	"I",	"K",	"L",	"M",
    "N",	"O",	"P",	"Q",	"R",
    "V",	"W",	"X",	"Y",	"Z"
]
k1 = [
    ["T",	"U",	"E",	"S",	"A"],
    ["B",	"C",	"D",	"F",	"G"],
    ["H",	"I",	"K",	"L",	"M"],
    ["N",	"O",	"P",	"Q",	"R"],
    ["V",	"W",	"X",	"Y",	"Z"]
]
def is_rectangle(p,p2):
    return (p[0]!=p2[0] and p[1]!=p2[1]),[p[0]!=p2[0],p[1]!=p2[1]]
def is_line(p,p2):
    return (p[0]==p2[0] or p[1]==p2[1]),[p[0]==p2[0],p[1]==p2[1]]
def val_to_x_y(p):
    return [int(p/5),p%5]
def calculate_line(srichka,X):
    a = val_to_x_y(k.index(srichka[0]))
    b = val_to_x_y(k.index(srichka[1]))
    a[X]+=1
    b[X]+=1
    if(b[X]>4):
        b[X] = 0
    if(a[X]>4):
        b[X] = 0
    return "".join([k1[a[0]][a[1]],k1[b[0]][b[1]]])
#QP UN GB QI KE
def calculate_square(srichka):
    a = srichka[0]
    b = srichka[1]
    a = val_to_x_y(k.index(a))
    b = val_to_x_y(k.index(b))
    x = a[1]
    a[1] = b[1]
    b[1] = x
    return "".join([k1[a[0]][a[1]],k1[b[0]][b[1]]])
def calculate(char1,char2):
    if is_line(val_to_x_y(k.index(char1)),val_to_x_y(k.index(char2)))[0]:
        _,flag = is_line(val_to_x_y(k.index(char1)),val_to_x_y(k.index(char2)))
        return calculate_line(char1+char2,flag[0])
    else:
        return calculate_square(char1+char2)
        

duma = input("Lines: ")
duma.split(" ")
duma = "".join(duma)
list_duma = list(duma)

flag = len(list_duma)%2==1
if(flag):
    list_duma.append("X")
x = []
for i in range(int(len(list_duma)/2+0.5)):
    x.append(calculate(list_duma[i*2],list_duma[i*2+1]))

print("".join(x))


