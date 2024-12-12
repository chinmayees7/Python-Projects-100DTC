import random
word_list = ["aardvark", "baboon", "camel","apple"]

chosen_Word = random.choice(word_list)
print(chosen_Word)

# len(chosen_Word)
for letter in range(len(chosen_Word)):
    print("_", end=" ")

#TODO 1: use a while loop to let the user guess again
#TODO 2:Change the for loop so that you keep the previous correct guess

game_over=False
correct_word=[]
while not game_over:
    guess=input("\nGuess a letter: ").lower()
    guess_word=''

    while len(guess)>1:
        print("Type a single letter please")
        guess=input("Guess a letter: ").lower()

    for i in chosen_Word:
        if i == guess:
            guess_word+=" "+i
            correct_word.append(guess)
        elif i in correct_word:
            guess_word+=i
        else:
            guess_word+=" _"

    print(guess_word)      
    print(correct_word)

    if "_" not in guess_word:
        game_over=True
        print("You win!")
           