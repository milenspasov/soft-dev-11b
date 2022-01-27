import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word

def play(word):
    allowed_errors = 6
    guesses = []
    done = False
    while not done:
        for letter in word:
            guess = input(f"Allowed errors left {allowed_errors}, Next Guess: ")
            guesses.append(guess.lower())
            if guess.lower() not in word.lower():
                allowed_errors -= 1
                if allowed_errors == 0:
                    break

            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")

            print("")


            done = True
            for letter in word:
                if letter.lower() not in guesses:
                    done = False


    if done:
        print(f"You found the word! {word}")
    else:
        print(f"Game over! word is {word}")

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
