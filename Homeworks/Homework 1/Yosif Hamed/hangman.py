import random

words=[
"weight",
"civilian",
"killer",
"reliance",
"ceremony",
"relief",
"elapse",
"toll",
"trivial",
"leadership"
]

word=random.choice(words)
err_counter=0
display_word=[]
for i in word:
    display_word.append("_")

print(" ".join(display_word))

while(1):
    guess=input()[0]
    if guess in word:
        for i in range(len(word)):
            if(word[i]==guess):
                display_word[i]=guess

    else:
        err_counter+=1
        print(10-err_counter,"tries left")
    if err_counter>=10:
        print("no more tries")
        break
    print(" ".join(display_word))
    if '_' not in display_word:
        print("You win")
        break