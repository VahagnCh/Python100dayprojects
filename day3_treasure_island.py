print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

crossroad =(input("Your are at a crossroad to the right you see a forest and to the left a lake, wich way do you want to move? Left or Right "))

if crossroad.lower() == "right":
    print("A group of bandits mugged you, GAME OVER!")
elif crossroad.lower() == "left":
    lake =(input("Welcome to the lake you can swim or wait, wich do you choose? swim or wait "))
    if lake.lower() == "wait":
        dors = input("Patience paid off, 3 dors have apeared a red one a blue one and a yellow one, wich one would you like to open? ")
        if dors.lower() == "yellow":
            print("You found the treasure! YOU WIN!")
        elif dors.lower() == "red":
            print("Im sorry you were shot by magic trap, GAME OVER!")
        elif dors.lower() == "blue":
            print("Sorry there is nothing behind this dor, GAME OVER!")
        else:
             print("You were not following the rules, GAME OVER!")
    else:
        print("While you were swiming the lake monster atacked you... GAME OVER!")
else:
    print("You were not following the rules, GAME OVER!")
