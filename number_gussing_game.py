# Number Guessing Game
print("---------------------------------------------------------------------------------------------------")
import random

betweennumber = int(input("Type a number : "))

guessnumber = random.randint(1, betweennumber)

chancecount = 3
if betweennumber < 10:
    print("Please! Enter The 10 Value up Number Choose")
    
else:
    while True:
        print("------------------------- Your Number -------------------------")
        usernumber = int(input("Gueess number of 1 to "+ str(betweennumber) +" : "))
        print()
        
        print("------------------------- Your Chance -------------------------")
        print("Chance is : ", chancecount)

        print("------------------------- Your Result -------------------------")
        if usernumber == guessnumber:
            print("Guessing Success")

            print("------------------------- You Play Game Again -------------------------")
            playagein = input("This Game play again (Y/N) : ")
            if playagein != "y":
                break
            chancecount = 3

        elif chancecount == 0:
            print("Sorry! Your Chance is : 0")
            print("Answer is : ", guessnumber)
        
            print("------------------------- You Play Game Again -------------------------")
            playagein = input("This Game play again (Y/N) : ")
            if playagein != "y":
                break
            chancecount = 3

        else:
            if guessnumber > usernumber:
                print("Guessing Low")

            elif guessnumber < usernumber:
                print("Guessing High")
            
            chancecount -= 1
        
        
        
    print("Thansk For play the Number Guess Game ")


print("---------------------------------------------------------------------------------------------------")