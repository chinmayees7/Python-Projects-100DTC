import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level :letters, symbols, numbers in sequence

password=''
for l in range(1,nr_letters+1):
    password+= random.choice(letters)

for s in range(1,nr_symbols+1):
    password+= random.choice(symbols)

for n in range(1,nr_numbers+1):
    password+= random.choice(numbers)

print(f"Your password is: {password}")

#Hard Level 1: no sequence in the characters

password=''
for l in range(1,nr_letters+1):
    password+= random.choice(letters)

for s in range(1,nr_symbols+1):
    password+= random.choice(symbols)

for n in range(1,nr_numbers+1):
    password+= random.choice(numbers)

print(len(password))
print(password)
password = random.sample(password, k=len(password))

print(type(password))
print((password))

print("Your password is: "+"".join(password))


#Hard Level 2: no sequence in the characters

password_list = []

for char in range(0, nr_letters ):
  password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
  password_list += random.choice(symbols)

for char in range(0, nr_numbers):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")