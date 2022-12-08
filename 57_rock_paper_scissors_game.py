"""
Rock Vs paper -> Paper Wins
Rock Vs scissor -> Rock Wins
paper vs Scissor -> Scissor Wins

"""

import random

l = ['rock', 'scissor', 'paper']

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game Start.....
    1. Yes | Play
    2. No | Exit'''))

    if uc == 1:
        for i in range(1, 6):
            userInput = int(input('''
            1. Rock
            2. Scissor
            3. Paper '''))

            if userInput == 1:
                uchoice = "rock"

            elif userInput == 2:
                uchoice = "scissor"

            elif userInput == 3:
                uchoice = "paper"

            Cchoice = random.choice(l)
            if uchoice == Cchoice:
                print("Computer Value ", Cchoice)
                print("User Value ", uchoice)
                print("Game Draw ")
                ucount = ucount + 1
                ccount = ccount + 1

            elif (uchoice == 'rock' and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (
                    uchoice == "scissor" and Cchoice == "paper"):
                print("User Value : ", uchoice)
                print("Computer Value : ", Cchoice)
                ucount = ucount + 1
                print(" You Win !!")

            elif (Cchoice == 'rock' and uchoice == "scissor") or (Cchoice == "paper" and uchoice == "rock") or (
                    Cchoice == "scissor" and uchoice == "paper"):
                print("User Value : ", uchoice)
                print("Computer Value : ", Cchoice)
                ccount = ccount + 1
                print(" Computer Win !!")

        if ucount == ccount:
            print("Match is Draw")
            print("user Score ", ucount)
            print("Computer Score", ccount)

        elif ucount >= ccount:
            print("Final Win the game !!")
            print("user Score ", ucount)
            print("Computer Score", ccount)

        elif ucount <= ccount:
            print("Final Win the game !!")
            print("user Score ", ucount)
            print("computer Score", ccount)
        else:
            print("Final Win the game !! ")
            print("user socre ", ucount)
            print("computer socre ", ccount)

    else:
        break
