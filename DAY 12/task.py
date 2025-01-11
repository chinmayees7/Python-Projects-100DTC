#Scope : acessing variables in different ways


#1. Local Scope
#player_health variable is a local scope here that can be accessed only under the function game()

def game():
    player_health=10
    print(player_health)

game()
print(player_health)

#2. Global Scope
#lives is global variable here that can be accessed anywhere in the code
lives=9
def cat():
    print(lives)

cat()
print(lives)


#cat_lives is a local function where as play is a global function

def play():
    def cat_lives():
        print(lives)

    cat_lives()
play()
cat_lives()