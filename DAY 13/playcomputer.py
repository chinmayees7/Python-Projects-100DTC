year = int(input("What is your birth year?"))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")


"""
Error: when 1994 is the input, nothing gets printed.

Explanation: 
1.if-else statements have conditions to check when the year is greater than 1980 and less than 1994 but not equal to them.
2.second condition is to check if the year is greater than 1994 but not equal to it.
This results to 1994 never being included to check ad=nd therefore no output is shown.

Solution:
1994 should be included either in millenial by changing the sign to <=1994 or in Gen Z by changing the sign to >=1994.
"""
if year > 1980 and year <=1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

#OR

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >=1994:
    print("You are a Gen Z.")

