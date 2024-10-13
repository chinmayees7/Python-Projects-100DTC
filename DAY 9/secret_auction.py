import art
print(art.logo)

def highest_bidder(bids):
    winner=''
    temp=0
    for key in bids:
        if bids[key]>temp:
            temp=bids[key]
            winner=key    
    print(f"The winner is: {winner} with a bid of Rs.{temp}.")

new_user=True
auction_dict={}

while new_user:
    name=input("What is your name? : ")
    bid=int(input("What is your amt to bid? : Rs. "))
    auction_dict[name]=bid

    other_user=input("Does anyone else want to bid: Yes or No: ").lower()
    if other_user=="no":
        new_user=False
        highest_bidder(auction_dict)
    elif other_user=="yes":
        print('\n'*100)
    

