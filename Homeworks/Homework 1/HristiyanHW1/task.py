import random
word_list = ["justice", "keyboard", "car", "metro", "computer", "school", "table", "telephone", "shop", "sunglassess"]
random_word = random.choice(word_list)
word_for_guessing = len(random_word) * "_"
is_word_guessed = False

count_mistakes = 0

print("Welcome to Hangman!")

while count_mistakes < 6:
    for downslash in word_for_guessing:
        print(f'{downslash} ', end=' ')
    print()
    letter = str(input("Guess you letter: "))
    
    count_index = 0
    is_letter_found = False
    
    for letter_searching in random_word:
        if letter_searching == letter:
            word_for_guessing = word_for_guessing[:count_index] + letter + word_for_guessing[count_index + 1:]
            is_letter_found = True
        count_index += 1
        
    if '_' not in word_for_guessing:
        is_word_guessed = True
        break
      
    if not is_letter_found:
        count_mistakes += 1

if is_word_guessed:
    print(f"You successfully guess the word {random_word.upper()}")   
else:
    print("Try again")
