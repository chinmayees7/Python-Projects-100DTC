states = ["Georgia", "Washington", "Hawaaii"]
state_At_index = len(states)
print(states[state_At_index])  

#IndexError: list index out of range

#to solve this : subtract 1 from the length since indexes start from 0
print(states[state_At_index-1])
