import random
word_list = ["aardvark", "baboon", "camel","apple"]

chosen_Word = random.choice(word_list)
print(chosen_Word)

#TODO 1: Create a "placeholder" with the same number of blanks as the chosen word.
# len(chosen_Word)
for letter in range(len(chosen_Word)):
    print("_", end=" ")

guess=input("\nGuess a letter: ").lower()

while len(guess)>1:
    print("Type a single letter please")
    guess=input("Guess a letter: ").lower()

#TODO 2: Create a "display" that puts the guess letter in the right blank.

for i in chosen_Word:
    if i == guess:
        print(i, end=" ")
    else:
        print("_",end=" ")
