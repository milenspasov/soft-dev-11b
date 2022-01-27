from random import choice

hangman = [
"""






===
""",
"""
 +
 |    
 |    
 |   
 |    
 |   
===
""",
"""
 +----+
 |    
 |    
 |   
 |  
 |   
===
""",
"""
 +----+
 |    |
 |    
 |   
 |  
 |   
===
""",
"""
 +----+
 |    |
 |    O
 |   
 |    
 |   
===
""",
"""
 +----+
 |    |
 |    O
 |    |
 |    |
 |   
===
""",
"""
 +----+
 |    |
 |    O
 |   /|
 |    |
 |   
===
""",
"""
 +----+
 |    |
 |    O
 |   /|\\
 |    |
 |   
===
""",
"""
 +----+
 |    |
 |    O
 |   /|\\
 |    |
 |   / 
===
""",
"""
 +----+
 |    |
 |    O
 |   /|\\
 |    |
 |   / \\
===
"""
]

word = choice(["administration", "admire", "underwear", "cat", "parrot", "dolphin", "whale", "agreement", "audience", "authority",
               "beautiful", "benefit", "business", "gadget", "campaign", "challenge", "character", "dog", "pet", "tail",
               "collection", "college", "colour", "honour", "beneficial", "company", "concert", "concern", "apple", "strawberry",
               "computer", "consideration", "cost", "cold", "customer", "daughter", "death", "development", "determine", "difficult",
               "different", "drive", "dawn", "field", "idea", "job", "lawyer", "laugh", "machine", "magazine",
               "memory", "treasure", "military", "morning", "movement", "necessary", "notice", "pattern", "outside", "person",
               "psychic", "plank", "remember", "responsibility", "safe", "rule", "return", "retail", "scene", "scientist",
               "security", "seek", "bee", "ant", "sense", "serious", "several", "shoulder", "show", "shoe",
               "significant", "similar", "simple", "sister", "brother", "father", "mother", "aunt", "uncle", "grandma",
               "grandpa", "cousin", "zoo", "technology", "television", "understand", "victim", "western", "witch", "wholesome"])

guessed = []
wrong = []

tries = 6

while tries > 0:
    a = ""
    for letter in word:
        if letter in guessed:
            a = a + letter
        else:
            a = a + "_ "
    if a == word:
        break
    print("Guess the word:", a)
    print(tries, "tries left")
    guess = input()
    if guess in guessed or guess in wrong:
        print("You have already guessed that letter!", guess)
    elif guess in word:
        print("You guessed right!")
        guessed.append(guess)
    else:
        print("You guessed wrong!")
        print(hangman[10 - tries])
        tries = tries - 1
        wrong.append(guess)
    print()
if tries:
    print("You guessed the word", word)
else:
    print("You didn't guess the word", word)
