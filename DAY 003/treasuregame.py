print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

#printing multi-lines use print('''  abc ''')

print('''
      Welcome to the Treasure Island! 
      Your mission is to find the treasure!
      ''')
turn = input('You\'re at a cross road. Take a turn "left" or "right" \n').lower()  #.lower() to turn the string to lowercase
# \'abc for adding quotes in the string : escape charater \
if turn =="left":
      choice = input('''You\'ve come to a lake.There is an island in the middle of the lake.
Type "wait" to wait for the boar. Type "swim" to swim across\n''').lower()   
       
      if choice == "wait":
            print("You've now crossed the lake!")
            color= input('There are 3 color doors: "red" , "yellow" and "blue". Pick one : \n').lower()
            if color == "yellow":
                 print('''You've found the treaure! 
                       YOU WIN !''')
            elif color == "red":
                 print('''You've burned by fire.! 
                       GAME OVERR !''')
            elif color == "blue":
                 print('''You are a dinner for the beasts! 
                       GAME OVER !''')
            else:
                 print('''There's no such door! 
                       GAME OVER!''')
      elif choice == "swim":
            print('''You\'ve been attacked by an angry trout.
                GAME OVER''')
      else: 
            print('''You can't do that ! 
                  GAME OVER !''')
            
elif turn == "right":
    print('''You fell in a hole. 
            GAME OVER''' )

    

