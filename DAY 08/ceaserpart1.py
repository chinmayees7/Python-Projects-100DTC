alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",'x',"y","z"]

direction=input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encyrpt()' that takes orginal_text and 'shift amount' as 2 inputs.
#TODO-2: Inside the 'encrypt' function , shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted message.
# You can use index() function to find out the postition of an item in a list

def encrpyt(original_text,shift_amount):
    msg=''

    for i in original_text:
        shift_letter_index=alphabet.index(i)+shift_amount
        
#TODO-4: What happens if you try to shift z forwards by 9?Can you fix the code?
        cipher_index=shift_letter_index % len(alphabet)
        msg+=alphabet[cipher_index]
    print(msg)



#TODO-3: Call the encrupt() function and pass in user inputs. You should be able to test the code and encrypt a message.
encrpyt(text,shift)