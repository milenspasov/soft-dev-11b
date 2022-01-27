from random import randint

words = ["acid",
         "changeable",
         "valuable",
         "desire",
         "furniture",
         "nutritious",
         "rich",
         "perpetual",
         "symptomatic",
         "agreement"]


def recreate():
    dict = {}
    stringer = ""
    x = ""

    for index, i in enumerate(list(words[randint(0, len(words))])):
        dict.setdefault(i, [])
        dict[i].append(index)
        x += '-'

    return x, dict


def guess(stringer, dict, guess):
    if guess in dict:
        for i in dict[guess]:
            lister = list(stringer)
            lister[i] = guess
            stringer = "".join(lister)
    else:
        print("Incorrect guess, try again...")

    return stringer


while True:
    print("Chosing new random word:")
    stringer, dict = recreate()

    while stringer.count('-') != 0:
        print(stringer)
        stringer = guess(stringer, dict, input("Guess your letter: "))
