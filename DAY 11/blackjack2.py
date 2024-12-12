import random
import art
def deal_card():
    """Return a random card from the deck"""
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

    card=random.choice(cards)
    return card

def calculate_Score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards) 

def compare(u_score, c_score): 
    if u_score == c_score:
        return "Draw !"
    elif c_score==0:
        return "You lost ! Computer has Blackjack !"
    elif u_score==0:
        return "You win ! You have a Blackjack!"
    elif u_score>21:
        return "You went overboard. You lost !"
    elif c_score>21:
        return "Computer went overboard. You win !"
    elif u_score> c_score:
        return "You win !"
    else:
        return "You lost !"

def play_game():

    print(art.logo)
    user_cards=[]
    computer_Cards=[]
    computer_score=-1
    user_Score=-1
    is_game_over=False


    for _ in range(2):
        user_cards.append(deal_card())
        computer_Cards.append(deal_card())

    while not is_game_over:
        user_Score=calculate_Score(user_cards)
        computer_score=calculate_Score(computer_Cards)
        print(f"Your cards: {user_cards}, Current Score: {user_Score}")
        print(f"Computer's first card: {computer_Cards[0]}")

        if user_Score==0 or computer_score==0 or user_Score>21:
            is_game_over=True
        else:
            user_should_deal=input("type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True


    while computer_score!=0 and computer_score < 17:
        computer_Cards.append(deal_card())
        computer_score=calculate_Score(computer_Cards)


    print(f"Your final hand: {user_cards}, Final Score: {user_Score}")
    print(f"Computer's final hand: {computer_Cards}, Final Score: {computer_score}")
    print(compare(user_Score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n': ").lower() =='y':
    print("\n" *100)
    play_game()

print("Thank you ! See you next time ! ")