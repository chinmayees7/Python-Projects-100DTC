print("Welcome to Python Pizza deliveries")
bill=0
size= input("What size of pizza do you want? S,M, or L: ")
if size == "S":
    print("Your pizza will cost $15")
    bill=15
elif size == "M":
    print("Your pizza will cost $20")
    bill=20
elif size == "L":
    print("Your pizza will cost $25")
    bill=25
else:
    print("Thats not a valid size")

pepperoni= input("Do you want pepperonion your pizza? Y or N: ")
if pepperoni == "Y":
        if size == "S":
            print("That will be extra $2")
            bill+=2
        else:
             print("That will be extra $3")
             bill+=3

extra_cheese= input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
        print("That will add another dollar in your bill")
        bill+=1

print(f"Your final bill is ${bill} ")
