#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",'x',"y","z"]

def caeser(direct,original_text,shift_amount):
    
    msg=''
    
    if direct== "decode":
            shift_amount*=-1
    
    for i in original_text:

#TODO-2: What happens if the user enters a number/symbol/space?        
        if i not in alphabet:
            msg+=i
        else:        
            shift_letter_index=alphabet.index(i)+shift_amount 
            cipher_index=shift_letter_index % len(alphabet)
            msg+=alphabet[cipher_index]

    print(f"Here is the {direct}d msg: {msg}")

#TODO-3: Can you figure out a way to restart the cipher program?

yes_or_no=True

while yes_or_no:
    
    direction=input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    
    caeser(direction,text,shift)

    restart= input("Type 'yes' if you want to continue or 'no' to quit.").lower()
    if restart=="no":
         yes_or_no=False
         print("Thank you !")