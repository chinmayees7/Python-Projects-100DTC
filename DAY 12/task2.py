# There is no block scope in python!
"""This means that variable created nested in other blocks of code eg. loops, if statements, while loops etc, dont get local scope. 
They are given function scope if they are within a function or global scope if they are not."""

game_level=10

enemies=["Skeleton", "Zombie", "Alien"]

def create_enemy():
    
    if game_level<5:
        new_enemy=enemies[0]
    
    print(new_enemy)

# new_enemy is given a function scope not a local scope meaning "if" statment didnt make it a local scope for "if".