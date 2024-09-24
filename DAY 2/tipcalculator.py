print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
total_tip=int(input("How much tip would you like to give? 10,12,or 15? "))
no_of_people=int(input("How  many people to split the bill? "))

tip= "{:.2f}".format((total_bill*(total_tip/100) +total_bill)/no_of_people)  #"{:.2f}".format is used when you need to compulsory display 2 decimals in case of 0s ,'
                                                                             #it converts integers to binary format
# #OR
tip= format(((total_bill*(total_tip/100) +total_bill)/no_of_people),".2f") 
print(f"Each person should pay: ${tip}")



