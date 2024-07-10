import random
l=["rock","scissor","paper"]

ucount=0
ccount=0

#Game to continue running
while True:
    uc=int(input('''
                Game Start....
                1 Yes
                2 No | Exit
                '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
                                1 Rock
                                2 Scissor
                                3 Paper
                                '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("You Win")
                ucount += 1
            else:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Computer Win")
                ccount += 1
        if ucount==ccount:
            print("Final Game Draw...")
            print("User Score", ucount)
            print("Computer Score", ccount)
        elif ucount>ccount:
            print("Final You Win the Game...")
            print("User Score", ucount)
            print("Computer Score", ccount)
        else:
            print("Final Computer Win the Game...")
            print("User Score", ucount)
            print("Computer Score", ccount)
            
    else:
        break
            
                