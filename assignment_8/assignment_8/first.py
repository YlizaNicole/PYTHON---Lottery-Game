#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import ran

def intro ():
    print ("Hello User! you're in luck! We're gonna play Lotto! ")
    name = input("what is your name?: ")
    name = name.title()
    print ("""Hello {}, welcome again to this program! enter your lucky numbers to win this game. Good Luck! """. format(name))

def user_input ():
    correct_guess = []
    for num in guessed_numbers:
        if num in generated:
            correct_guess.append(num)
            
            print('your correct guesses  are', correct_guess)
            print('you guessed ', guessed_numbers)
            print('the supposed are ', generated)