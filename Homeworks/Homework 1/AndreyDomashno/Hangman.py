import random

words = ("administration", "admire", "underwear", "cat", "parrot", "dolphin", "whale", "agreement", "audience", "authority",
               "beautiful", "benefit", "business", "gadget", "campaign", "challenge", "character", "dog", "pet", "tail",
               "collection", "college", "colour", "honour", "beneficial", "company", "concert", "concern", "apple", "strawberry",
               "computer", "consideration", "cost", "cold", "customer", "daughter", "death", "development", "determine", "difficult",
               "different", "drive", "dawn", "field", "idea", "job", "lawyer", "laugh", "machine", "magazine",
               "memory", "treasure", "military", "morning", "movement", "necessary", "notice", "pattern", "outside", "person",
               "psychic", "plank", "remember", "responsibility", "safe", "rule", "return", "retail", "scene", "scientist",
               "security", "seek", "bee", "ant", "sense", "serious", "several", "shoulder", "show", "shoe",
               "significant", "similar", "simple", "sister", "brother", "father", "mother", "aunt", "uncle", "grandma",
               "grandpa", "cousin", "zoo", "technology", "television", "understand", "victim", "western", "witch", "wholesome")

game_check = 1;

word = words[random.randint(0,len(words)-1)]

find = []
for i in range(len(word)):
        find+="_"
hp=6
#print(word)
while(game_check):
    check=1
    
    for i in find:
        print(i, end = ' ')
    print("\nRemaining HP - "+str(hp))     
    letter = str(input("Guess your letter: "))
    for i in range(len(word)):
        if(word[i]==letter):
            find[i]=letter
            check = 0;
    if(check):
        hp-=1
        
    if('_' not in find):
        print(word)
        print("You Win!")
        break
    elif(hp==0): 
        print("You lose! The word was "+word)
        break
    print()
