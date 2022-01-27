from random import randint
words = ["scholar",
"articulate",
"duty",
"tease",
"achieve",
"predator",
"capture",
"explain",
"potential",
"sausage"]


def recreate():
    dict = {}
    stringer = ""
    x = ""
    for index,i in enumerate(list(words[randint(0,len(words))])):
        dict.setdefault(i,[])
        dict[i].append(index)
        x+='_'
    return x,dict

def guess(stringer,dict,guess):
    if guess in dict:
        for i in dict[guess]:
            lister = list(stringer)
            lister[i] = guess
            stringer = "".join(lister);
    return stringer


print("Welcome to Hangman!:")
while True:
    print("Chosing new random word:")
    stringer,dict =  recreate()
    while stringer.count('_') != 0:
        print(stringer)
        stringer = guess(stringer,dict,input("Guess: "))
