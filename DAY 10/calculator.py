import art
print(art.logo)

#TODO -1 :Write out the operations functions- add, subtract, multipy and divide.

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

#TODO -2:Store these functions into a dictionary as the values. Keys= "+", "-", "*", "/"

operations_dict={
    "+":add,  
    "-":subtract,
    "*":multiply,
    "/":divide,
}

#TODO -3: Use the dictionary operations to perform the calculations. Multipy 4*8 using the dictionary

# print(operations_dict["*"](4,8))

"""Functionality:

• Program asks the user to type the first number.

• Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")

• Program asks the user to type the second number.

• Program works out the result based on the chosen mathematical operator.

•Program asks if the user wants to continue working with the previous result.

•If yes, program loops to use the previous result as the first number and then repeats the calculation process.

•If no, program asks the user for the first number again and wipes all memory of previous calculations ."""

def calculator():

    should_accumlate=True
    num1=float(input("What is the first number? "))

    while should_accumlate:

        for op in operations_dict:
            print(op)

        operation=input("Choose a mathematical operation : " )
        if operation not in operations_dict:
            print("Please show a valid operation!To try again re-run!")
            return
        num2=float(input("What is the next number? "))

        result=operations_dict[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")

        exit=input("Do you want to try again?'y'or 'n': ").lower()
        if exit=="n":
            print("Thank you for using my calculator!")
            return
        elif exit=="y":
            should_continue=input("Do you want to continue with the previous result?'y' or 'n': ").lower()
            if should_continue=="n":
                should_accumlate=False
                print("\n"*100)
                print(art.logo)
                calculator()
            elif should_continue=="y":
                num1=result
            else:
                print("Invalid Text!.Please run again! ")
                return
        else:
            print("Invalid Text!.Please run again! ")
            return

calculator()