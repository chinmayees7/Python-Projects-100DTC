import random  #random module for generating random numbers

# randome_integer = random.randint(1,10)  #includes numbers between 1 & 10
# print(randome_integer)

# random_number_0_to_1 = random.random() *10  #0.0 <= X <1.0
# print(random_number_0_to_1)


# random_float = random.uniform(1,10)  # a <= N <= b  random.uniform(a,b)
# print(random_float) 

n= random.randint(0,1)  #0= heads ; 1=tails
if n==0:
    print("heads")
else:
    print("tails")