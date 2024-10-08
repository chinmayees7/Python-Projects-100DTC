alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",'x',"y","z"]

direction=input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

def encrpyt(original_text,shift_amount):
    msg=''

    for i in original_text:
        shift_letter_index=alphabet.index(i)+shift_amount

        cipher_index=shift_letter_index % len(alphabet)
        msg+=alphabet[cipher_index]
    print(msg)

# encrpyt(text,shift)

#TODO-1:Create a function called decrypt()  that takes original_text and shift_amount as 2 inputs
#TODO-2: Inside the decrypt() function, shift each letter of the original_text backwards in the alphabet by the shift_Amount and print the decrupted text.

def decrypt(original_text, shift_amount):
    msg=''

    for i in original_text:
        shift_letter_index=alphabet.index(i)-shift_amount
        cipher_index=shift_letter_index % len(alphabet)
        msg+=alphabet[cipher_index]  
    print(msg)


# decrypt(text,shift)

#TODO-3: Combine the encrypt() and decrypt() functions into a single function called caeser().
#  Use the value of the user chosen direction variable to dertermine which functionality to use.
#  Call the caeser function instead of encrypt/decrypt and pass all three variables : direction/text/shift

def caeser(direct,original_text,shift_amount):
    
    msg=''
    
    if direct== "decode":
            shift_amount*=-1

    for i in original_text:
        
        shift_letter_index=alphabet.index(i)+shift_amount 
        cipher_index=shift_letter_index % len(alphabet)
        msg+=alphabet[cipher_index]
        
    print(f"Here is the {direct}d msg: {msg}")

caeser(direction,text,shift)