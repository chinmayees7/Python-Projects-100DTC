import hangman_art
import hangman_words
import random

print(f"\n{hangman_art.logo}")
chosen_Word = random.choice(hangman_words.hangman_words)
print(chosen_Word)
# len(chosen_Word)
print("Word to guess: ")
for letter in range(len(chosen_Word)):
    print("_", end=" ")

game_over=False

lives=6
correct_word=[]
incorrect_letters=[]
while not game_over :
    guess=input("\n\nGuess a letter: ").lower()
    guess_word=''

    while len(guess)>1:
        print("Type a single letter please!!")
        guess=input("\n\nGuess a letter: ").lower()


    if guess in correct_word or guess in incorrect_letters:
        print("\nYou have already chosen this letter!")

    if guess in chosen_Word:
        print(f"\nThat's right! '{guess}' exists in the word!")

    for i in chosen_Word:
        if i == guess:
            guess_word+=i+" "
            correct_word.append(guess)
        elif i in correct_word:
            guess_word+=i +" "
        else:
            guess_word+="_ "
    
    if guess not in chosen_Word:
        print(f"\n'{guess}' is not a letter in the word! UH OH! Life is reduced by 1 ")
        lives-=1
        incorrect_letters.append(guess)

    print(f"\n {guess_word}") 
    print(hangman_art.stages[lives])
    print(f"\n----------------------------------------Lives: {lives}/6--------------------------------------------------------\n")
    print("Word to guess: ")
    print(f"\n {guess_word}") 
    

    if "_" not in guess_word:
        game_over=True
        print("\nYou win!")
    if lives == 0:
        game_over=True
        print("\nYou lost!")
        print(f"\nThe correct word is: {chosen_Word}\n")
