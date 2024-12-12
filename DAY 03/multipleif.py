#photo extra charges in the rollercoaster ride

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
bill=0

if height >= 120:
    print("You can ride it!")
    age= int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill=5
    elif age <=18:
        print("Youth tickets are $7.")
        bill=7
    else:
        print("Adult tickets are $12.")
        bill=12
        
    photo= input("Do you want a photo taken? Y or N ? ")

    if photo == "Y" or "y":
        bill +=3
    
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you are not tall enough to ride it!")