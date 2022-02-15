#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import re
import random

def intro ():
    print ("Hello User! you're in luck! We're gonna play Lotto! ")
    name = input("what is your name?: ")
    name = name.title()
    print ("""Hello {}, welcome again to this program! enter your 3 lucky numbers to win this game. Good Luck! """. format(name))


def check(answer, lottonum):
    if  (answer == lottonum):
        print ("\nWinner Winner! Chicken Dinner\n")
    else:
        print ("\nYou lose\n")



def getanswer():
    answer = []

    for x in range(3):
        nums = int(input("Pick a number 0 through 9: "))
        if 0 <= nums <= 9:
            answer.append(nums)
        else:
            input("Invalid input")
            

            
    return sorted(answer)

def getlottonum():
    ran = random.sample(range(0,9), 3)
    ran.append
    return sorted (ran)

def main():
    answer = getanswer()
    lottonum = getlottonum() 
    check(answer, lottonum)

intro ()
main()

again = str(input("Do you want to play again (type y/n): ")).lower()
if again == "y":
    main ()
else:
    exit ()