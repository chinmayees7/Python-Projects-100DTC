stages=[''' 
    _____________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |
    |___''',
     
     '''
    _____________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
    |___''',

    '''
    _____________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
    |___''',
     
     '''
    _____________
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
    |___''',

    '''
    _____________
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
    |___''',
     
     '''
    _____________
    |/      |
    |      (_)
    |      
    |      
    |      
    |
    |___''',

    '''
    _____________
    |/      |
    |      
    |      
    |      
    |      
    |
    |___''']

import random
word_list = ["aardvark", "baboon", "camel","apple"]

chosen_Word = random.choice(word_list)
print(chosen_Word)

# len(chosen_Word)
for letter in range(len(chosen_Word)):
    print("_", end=" ")

game_over=False

#TODO 1: Create a variable called "lives " to keep track of the lives left
#Set lives to 6

lives=6
correct_word=[]
incorrect_letters=[]
while not game_over :
    guess=input("\nGuess a letter: ").lower()
    guess_word=''
    
    while len(guess)>1:
        print("Type a single letter please")
        guess=input("Guess a letter: ").lower()
        
    if guess in correct_word or guess in incorrect_letters:
        print("You have already chosen this letter!")

    for i in chosen_Word:
        if i == guess:
            guess_word+=" "+i
            correct_word.append(guess)
        elif i in correct_word:
            guess_word+=i
        else:
            guess_word+=" _"

#TODO 2: if guess is not a letter in the chosen word, the life is reduced by 1
#if lives goes down to 0 then the game should stop and it should print "You lose"   

    if guess not in chosen_Word:
        print("This is not a letter in the word! Life is reduced by 1 ")
        lives-=1
        incorrect_letters.append(guess)


#TODO 3: print the ASCII art from 'stages' that corresponds to the current number of lives the user has remaining.


    print(f"Lives: {lives} {stages[lives]}")
    print(guess_word)      
    # print(correct_word)

    if "_" not in guess_word:
        game_over=True
        print("You win!")
    if lives == 0:
        game_over=True
        print("You lose")