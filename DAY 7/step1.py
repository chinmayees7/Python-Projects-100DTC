#TODO 1: Randomly choose a word from word_list and assign it to a variable called chosen_word. Then print it.

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_Word = random.choice(word_list)
print(chosen_Word)

#TODO 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess=input("Guess a letter: ").lower()

while len(guess)>1:
    print("Type a single letter please")
    guess=input("Guess a letter: ").lower()

#TODO 3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.Print "Right" if it is "Wrong " if it is not.

for i in chosen_Word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
