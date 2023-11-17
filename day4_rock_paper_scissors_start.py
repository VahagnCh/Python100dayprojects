import random

rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''
chosen_hand = input("What do you choose Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
options = ["rock", "paper", "scissors"]

if int(chosen_hand) == 0:
    print(rock)
    print("Computer chose: ")
    for i in range(1):
        if (random.choice(options)) == 'rock':
            print(rock)
            print("It's a draw")
        elif (random.choice(options)) == 'scissors':
            print(scissors)
            print("You win!")
        else:
            print(paper)
            print("You lose.")
elif int(chosen_hand) == 1:
    print(paper)
    print("Computer chose: ")
    for i in range(1):
        if (random.choice(options)) == 'rock':
            print(rock)
            print("You win!")
        elif (random.choice(options)) == 'scissors':
            print(scissors)
            print("You lose.")
        else:
            print(paper)
            print("It's a draw.")
elif int(chosen_hand) == 2:
    print(scissors)
    print("Computer chose: ")
    for i in range(1):
        if (random.choice(options)) == 'rock':
            print(rock)
            print("You lose.")
        elif (random.choice(options)) == 'scissors':
            print(scissors)
            print("It's a draw.")
        else:
            print(paper)
            print("You win!")
else:
    print("You typed an invalid number, try again with 0 for Rock, 1 for Paper or 2 for Scissors.")

