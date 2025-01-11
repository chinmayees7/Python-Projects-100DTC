""" Avoid modifying Global Scopes since it creates confusion. You can read it and use it."""

enemies=1 #variable 1

def increase_enemies():
    enemies=2 #variable 2
    print(f"Enemies inside the function:{enemies}")

increase_enemies()
print(f"Enemies outside the fucntion{enemies}")

#variable 1 and 2 are completely different, you arent modifying the global varaible 1

#incase you want to modify a global variable "global" keyword is to be used"
friends=2

def increase_friends():
    global friends
    friends=3
    print(f"Friends insidde the function:{friends}")

increase_friends()
print(f"Friends outside the function:{friends}")

#another way to do this using return statement, here there's no need to use global keyword

comp_enemies=2
def decrease_comp_enemies():
    print(f"Comp enemies inside the function:{comp_enemies}")
    return comp_enemies-1

comp_enemies=decrease_comp_enemies()
print(f"Comp enemies ouside the function:{comp_enemies}")