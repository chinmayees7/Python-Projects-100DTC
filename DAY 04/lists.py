# Data structure : List  : fruits = ["mango", "apple"]

states_of_America= ["Delaware","Pensalvania", "New Jersey" , "Georgia"]
print(states_of_America[0])  #element at 1 = delaware
print(states_of_America[-1])  #element at last = georgia

states_of_America[3] = "Hawaii"  # mutable
states_of_America.append("Kingston")  # adding element at the end of the list
print(states_of_America)

states_of_America.extend(["Mexxico","New York"])  #adding multiple list elements to the currentlist at the end
print(states_of_America)