#converting data types
print(int("123") +int("456"))

# print(int('abc')) #ValueError: invalid literal for int() with base 10: 'abc'

#task: print("numbers of letters in your name: " +len(input("enter your name"))) , make this error free
print("numbers of letters in your name: " +str(len(input("enter your name"))))  #can only concatenate same data type 
      