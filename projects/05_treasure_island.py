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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Choice1 = input("You are greeted by a cross road, which way will you choose. Left or right?")

if Choice1 == "right" or Choice1 == "Right" or Choice1 == "RIGHT":
    print("You run to the right and fall into a pit of darkness. GAME OVER.")
elif Choice1 == "left" or Choice1 == "Left" or Choice1 == "LEFT":
    Choice2 = input("You run to the left to which felt like an eternity. You are then greeted by a lake. You can wait for a boat or swim across.")
    if Choice2 == "swim" or Choice2 == "Swim" or Choice2 == "SWIM":
        print("While stroking to the island, you are attack by an angry salmon. GAME OVER.")
    elif Choice2 == Choice2 == "wait" or Choice2 == "Wait" or Choice2 == "WAIT":
        Choice3 = input("You made it to the island with wet clothing. And there is a house that catches your attention. You find that there are 3 doors, one red, one yellow, one blue. Which one do you open?")
        if Choice3 == "red" or Choice3 == "Red" or Choice3 == "RED":
            print("You open the red door and instinctivly walk inside it without thinking. You burn to death while noticing the room was full of fire. GAME OVER.")
        elif Choice3 == "blue" or Choice3 == "Blue" or Choice3 == "BLUE":
            print("You open the blue door and instinctivly walk in. You are greeted by a swarm of beast hanging from the sealing and eat you alive. GAME OVER.")
        elif Choice3 == "yellow" or Choice3 == "Yellow" or Choice3 == "YELLOW":
            print("You open the yellwo door and instinctivly walk in. You take a sighn of releaf as you notice you found the treasure! YOU WIN!")
        else:
            print("A bird opens the door with its wings and eats your ear off for misspelling a word. GAME OVER.")
    else:
        print("An angry ant bite your head of for misspelling a word. GAME OVER.")
else:
     print("An angry lion attacked you for missspelling a word. GAME OVER.")