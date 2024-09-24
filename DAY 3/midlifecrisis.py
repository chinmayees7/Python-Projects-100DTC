#midlife crisis of age 45-55 will get free rides and no cost of photos

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
    elif age >=45 and age <=55:  #else  45 <= age <=55 in less wordy method
        print("You are free to ride this rollercoaster cuz you are already riding yourself crazy!")
    else:
        print("Adult tickets are $12.")
        bill=12
        
    photo= input("Do you want a photo taken? Y or N ? ")

    if photo == "Y" or "y":
        if not age >=45 and age <=55:  #since mid-life wont have to pay for photo as well
            bill +=3
    
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you are not tall enough to ride it!")