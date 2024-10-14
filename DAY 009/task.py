#Dictionary :  {Key:Value} eg. {Name:"Chin"}
Loop=''
programming_dictionary = {
    "Bug":"A bug is an unexpected problem with software or hardware",
    "Function":"A function is a sequence of commands that can be reused together later in a program",    
}

#printing a value
print(programming_dictionary["Function"])

#printing all keys and values
print(programming_dictionary)

#adding an element
programming_dictionary["Loop"]="a loop is a sequence of instruction s that is continually repeated until a certain condition is reached"

#defining a empty dictionary
empty_dict={}

#Wiping a dictionary
programming_dictionary={}

#Edit an item 
programming_dictionary["Bug"]="A moth in your computer"

print(programming_dictionary)

#Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) #retrival of values