def my_fucntion():
    for i in range(1,20):
        if i==20:
            print("You got it")

my_fucntion()

#Describe the problem-  
""" this function iterates with the value of i starting from 1 and ending at 19. if the value of i is 20 , "You got it" will be printed. 
The assumption is made that i will reach the value of 20 to print out the statement. But the range() function includes the lower bound but excludes the upper bound."""

def my_fucntion():
    for i in range(1,21):
        if i==20:
            print("You got it")

my_fucntion()