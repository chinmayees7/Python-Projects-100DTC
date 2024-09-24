import random
rock='''
        ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper ='''
        PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
        SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images= [rock, paper,scissors]

#code 1 : 

choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper , 2 for Scissors: "))
print(f"You chose: {choice}")

if 0 <= choice <=3 :

    print(images[choice])  
 
    comp_choice=random.randint(0,2)
    print(f"Computer chose: {comp_choice} ")

    print(images[comp_choice])

    if choice == comp_choice:
        print("\tIt's a DRAW!\n")

    elif choice==0 and comp_choice ==1 or choice==1 and comp_choice==2 or choice==2 and comp_choice==0 :
        print("\tYou lost!\n")

    else:
        print("\tYou Won!\n")

else:
    print("Invalid Choice!")

# code 2 : better choice

loss= [[0,1],[1,2],[2,0]]

choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper , 2 for Scissors: "))

if 0 <= choice <= 3:

    print(images[choice])

    comp_choice=random.randint(0,2)
    print(f"Computer chose: {comp_choice}")
    print(images[comp_choice])

    if comp_choice == choice:
        print("\tIt's a Draw\n")
    else: 
        choice_list=[choice,comp_choice]

        if choice_list in loss:
            print("\tYou Lost!\n")
        else:
            print("\tYou Won!\n")        
else:
    print("Invalid choice!")