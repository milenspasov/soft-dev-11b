import random

words = ["WATER","FALL","HANGMAN",
		"SNOW","BOY","COMPUTER",
		"BALKAN","ANDROID","FORTNITE","MURDA"]
word = random.choice(words)

word_new = ""

print("Welcome to Hangman!")

# Make empty word with _
for i in range(len(word)):
	word_new += "_"

print(word_new)

# find function
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

# loop
counter = 0
more_tries = 6
correct_pos = []

while counter < 6:

	#if we guessed the word
	if(word_new.find("_") == -1):
		counter = 6
		print("Congratulations! You guessed the word!")
		exit()

	print("Guess your letter: ",end="")
	
	#Inputting letter
	x = input()
	
	#returns list of positions of found characters
	j = list(find(word,x))
	
	#if we found letter/s
	if(len(j) > 0):
		for i in range(len(j)):
			pos = j[i] 
			word_new = list(word_new)
			word_new[pos] = x
			word_new = "".join(word_new)
		print(word_new)
	else:
		more_tries-=1
		counter+=1
		if more_tries == 0:
			print("Sorry, you lost. The word was " + word + ".")
			break
		print("Incorrect! You have ",end="")
		print(more_tries,end="")
		print(" more tries.")