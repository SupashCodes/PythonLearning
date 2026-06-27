import random
import math
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("------Welcome to the game------")

print("You have entered the treasure island. You have two ways to go to: left or right. type l for left and r for right")
a = input()
if a == "l":
    print("you have entered in a cave and you got killed by a tiger")

if a=="r":
    print("you are now in a palace")
    print("You have three doors to choose from: red, blue and green: type r for red, b for blue and g for green")
    a = input()
    if a == "r":
        print("You have won")

    if a == "b":
        print("There is fire in this room and you have died due to it")

    if a == "g":
        print("You have been eaten alive by a crocodile")

    else:
        print("You have entered an invalid character")

else:
    print("You have entered an invalid character")

print("-----Game Over-----")

