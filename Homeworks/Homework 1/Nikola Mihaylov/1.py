from random import choice

s = choice(["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHT", "NINTH", "TENTH"])
found = ['_'] * len(s)
attempts = 6

print("Welcome to Hangman!")
print("".join(c + ' ' for c in found))
while attempts > 0 and "".join(found) != s:
    flg = False
    guess = input("Guess your letter: ")[0].upper()
    for i, c in enumerate(s):
        if c == guess:
            flg = True
            found[i] = c
    
    if flg:
        print("".join(c + ' ' for c in found))
    else:
        attempts -= 1
        print("Incorrect!")
