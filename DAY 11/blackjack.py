import art
import random

play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

while play=='y':
    
    print(art.logo)

    passed=True
    your_cards=[random.choice(cards),random.choice(cards)]
    current_Score=sum(your_cards)
    comp_cards=[random.choice(cards),random.choice(cards)]
    comp_sum=sum(comp_cards)
    
    while passed:
        print(f"Your cards: {your_cards}")
        print(f"Current score: {current_Score}")

        
        if comp_sum==21:
            print(f"Computer's cards: {comp_cards}")
            print(f"Computer's sum : {comp_sum}")
            print("You lose ! Computer hit Blackjack! ")
            break
        elif current_Score==21:
            print("You win ! You hit Blacjack!")
            break
        elif current_Score>21:
            print("You went overboard ! You lose !!")
            break
        print(f"Computer's first card: {comp_cards[0]}")

        new=input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if new=='y':
            your_cards.append(random.choice(cards))
            
            if your_cards[-1]==11: 
                if current_Score>21:
                    your_cards[-1]=1
                else:
                    your_cards[-1]=11 
            current_Score=sum(your_cards)


        elif new=='n':
            
            while comp_sum<16:
                comp_cards.append(random.choice(cards))
                comp_sum=sum(comp_cards)

            print(f"Computer's cards: {comp_cards}, Computer score: {comp_sum}")
            if comp_sum>21:
                print("You win ! Computer went overboard !!")
                break
            elif comp_sum==current_Score:
                print("Its a draw !")
                break
            elif comp_sum>current_Score:
                print("Computer wins !")
                break
            else:
                print("You win !")
                break
            
    print("Thank you for playing !")   
    play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play=='y':
        print("\n" *100)

print("okay! see you next time!")    
    
    


    

    
