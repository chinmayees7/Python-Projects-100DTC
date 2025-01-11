import art
import random

print(art.logo)
print("Welcome to the game !")
print("I am thinking of a number between 1 and 100.")

generated_number=random.randint(1,100)
lives=0

def function():

    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty=="easy":
        return lives+10
    elif difficulty=='hard':
        return lives+5
    return 0


def play():

    lives=function()

    if lives==0:
        print("Please choose a valid choice!")
        play()

    global generated_number
    flag=1
 
    while flag==1:

        print(f"You have {lives} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))

        if guess!=generated_number:
            
            lives=lives-1

            if lives==0:
                print("You lost! You don't have any lives left!")
                flag=0
                break

            if guess< generated_number:
                print("Too low.")
            elif guess>generated_number:
                print("Too high.")
            print("Guess again.")
            
        else:
            print("You got it!")
            print(f"The number was {generated_number}. Congrats!")
            flag=0
    
play()