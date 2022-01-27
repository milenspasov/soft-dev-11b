import random

def choose_word(words, words_num):
    word_index = random.randrange(0, (words_num - 1))
    word = words[word_index]
    
    return word


words = [
    'book',
    'iron',
    'car',
    'door',
    'phone',
    'computer',
    'cup',
    'bike',
    'smile',
    'agile'
]

word = choose_word(words, 10)
word_len = len(word)
word_guesser = list('_' * word_len)
counter = 0
letters_found = 0

while True:
    word_guesser = "".join(word_guesser)
    print(word_guesser)

    if letters_found == word_len:
        break

    letter = input('Guess your letter: ')

    counter = 0
    if letter in word:
        for i in word:
            if i == letter:
                word_guesser = list(word_guesser)
                word_guesser[counter] = i
                letters_found += 1
            counter += 1
    else:
        print('Incorrect!')
    