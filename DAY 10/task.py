#Functions with ouputs

def format_name(f_name,l_name):
    """Take a first name and a last name and format it to return the
    title case version of the name. """  #Docstring = definition of a function written after a function is declared to document the code.
    #Point your cursor to format_name (where the function is defined & called) and you can find the docstring as a definition
    if f_name=='' or l_name=='':
        return "You did not provide valid inputs"  #if the input is empty escape from the function
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    return f" Result:{formated_f_name} {formated_l_name}"


formated_String=format_name(input("What is your first name?"), input("What is your last name? "))
print(formated_String)


def function1(text):
    return text+text

def function2(text):
    return text.title()
    print("hi") #wont be printed because return is the end of the function

output=function2(function1("hello"))
print(output)
