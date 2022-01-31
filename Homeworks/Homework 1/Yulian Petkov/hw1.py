import random

words = ["apple", "banana", "cherry", "swag", "street", "operation", "force", "police", "signature", "monkey"]
chosen_word = random.choice(words)
word_len = len(chosen_word)
hidden_word = '_' * word_len
print("Number of letters: ", word_len)
print(" ".join(hidden_word))
wrong = 0
fail = 0

chosen_list = list(chosen_word)
hidden_list = list(hidden_word)

while(fail != 6 or hidden_word != chosen_word):
	count = 0
	for z in range(word_len):
		if hidden_list[z] == chosen_list[z]:
			count = count + 1
			if count == word_len:
				print("success")
				exit()

			

	letter = input("Guess a letter: ")
	wrong = 0
	for x in range(word_len):
		if letter == chosen_list[x] and letter == hidden_list[x]:
			print("Already guessed")
		elif letter == chosen_list[x]:
			hidden_list[x] = chosen_list[x]
		elif letter != chosen_list[x]:
			wrong = wrong + 1
			#print("wrong", wrong)
			if wrong == word_len:
				fail = fail + 1
				if fail == 6:
					print("gubish glupak")
					exit()
			#print("fail", fail)
	hidden_word = "".join(hidden_list)
	print(" ".join(hidden_word))
	

			




