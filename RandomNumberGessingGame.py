import random

#computer numbers logic
Cnumber=random.randrange(1,101)

#enter user number
userInput=int(input("enter your number:--"))

#Using if elif else statement
if userInput>Cnumber:
    print("Computer Number", Cnumber)
    print("Your guess number is High")
elif Cnumber>userInput:
    print("Computer Number",Cnumber)
    print("Your guess number is too Low")
else:
    print("Computer Number",Cnumber)
    print("Your guess number is Equal")