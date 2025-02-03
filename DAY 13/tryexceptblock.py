try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical value such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}")