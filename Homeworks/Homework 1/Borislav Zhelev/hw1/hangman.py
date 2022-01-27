import random

words = ["administration", "admire", "underwear", "cat", "parrot", "dolphin", "whale", "agreement", "audience", "authority",
        "beautiful", "benefit", "business", "gadget", "campaign", "challenge", "character", "dog", "pet", "tail",
        "collection", "college", "colour", "honour", "beneficial", "company", "concert", "concern", "apple", "strawberry",
        "computer", "consideration", "cost", "cold", "customer", "daughter", "death", "development", "determine", "difficult",
        "different", "drive", "dawn", "field", "idea", "job", "lawyer", "laugh", "machine", "magazine",
        "memory", "treasure", "military", "morning", "movement", "necessary", "notice", "pattern", "outside", "person",
        "psychic", "plank", "remember", "responsibility", "safe", "rule", "return", "retail", "scene", "scientist",
        "security", "seek", "bee", "ant", "sense", "serious", "several", "shoulder", "show", "shoe",
        "significant", "similar", "simple", "sister", "brother", "father", "mother", "aunt", "uncle", "grandma",
        "grandpa", "cousin", "zoo", "technology", "television", "understand", "victim", "western", "witch", "wholesome"]

def get_word():
    word = random.choice(words)
    return word.upper()

def play(word):
    word_completion = "_"*len(word)
    guess = False
    guessed_l = []
    lives = 6
    print(word_completion)
    print('\n')
    
    while not guess and lives > 0:
        symbol = input("enter symbol:  ").upper()
        if symbol in guessed_l:
            print("Already guessed")
        elif symbol not in word:
            print("Incorect letter")
            lives -= 1
            guessed_l.append(symbol)
        else:
            guessed_l.append(symbol)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == symbol]
            for index in indices:
                word_as_list[index] = symbol
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guess = True
        print(word_completion)
    print("the word was:")
    print(word)

def main():
    word = get_word()
    play(word)
    while input("play again? (Y/N)").upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()