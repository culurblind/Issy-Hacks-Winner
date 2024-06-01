# Craps.py is a python file that runs the back end code for the casino game craps
# it contains functions that print text slowly, clear the terminal, check if an input is a number, and also a method for rolling the dice 
# and the main function where the actual game runs, returning the new balance

import random
import time
import os
#craps

#prints given string slowly
#default delay of 0.1s if no delay peramter is given
def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.05

    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# clear_terminal() func clears the terminal after every round
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# isnt_int func makes sure an input is a int
def isnt_int(raw_inp):
    if(not raw_inp.isdigit()):
        return True

#rolls dice and adds them up
def dicetotal():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def craps(balance):
    slow_print("Welcome to Craps! Your goal is to see whether the dice will roll a winning number.")
    slow_print("In the first round, if you roll a 7 or 11, you win. If you roll a 2, 3, or 12, you automatically lose.")
    slow_print("Any other combination of values will be added to the point, and you will continue rerolling until you get that number again or roll a 7, in which you lose")
    print()
    time.sleep(3)

    gameplay = True
    while gameplay == True:

        placeHolder = True
        while (placeHolder):
            slow_print("You have a balance of: " + str(balance))
            slow_print("How much do you want to bet? ")
            bet = input()
            clear_terminal()

            if isnt_int(bet):
                slow_print("Please enter a valid integer to bet on.")

            elif int(bet) > balance:
                slow_print("Slow your roll there pal, you don't have " + str(bet) + ".")

            else:
                placeHolder = False
                bet = int(bet)
                balance -= bet

        diceNum = dicetotal()
        input("Alright, betting " + str(bet) + ". Press enter to roll.")
        clear_terminal()
        slow_print("Rolling... Rolling... Rolling... ", 0.1)
        clear_terminal()

        if diceNum == 7 or diceNum == 11:
            slow_print("The dice rolled " + str(diceNum) + ", You won!")
            balance += 2 * bet
        
        elif diceNum == 2 or diceNum == 3 or diceNum == 12:
            slow_print("You lost the bet, the dice rolled " + str(diceNum))
        
        else:
            print("you rolled " + str(diceNum) + " the die will reroll")
            #true/flase for if a number is rerolled
            pastNumber = False

            print()
            while pastNumber == False:
                time.sleep(0.55)
                input("Press enter to roll.")
                clear_terminal()
                slow_print("Rolling... Rolling... Rolling... ", 0.1)
                newNum = dicetotal()
                if newNum == diceNum:
                    slow_print("You rerolled " + str(diceNum) + " again! You win!")
                    pastNumber == True
                    balance += 2 * bet
                    break
                elif newNum == 7:
                    slow_print("You rolled a 7! You have lost the game")
                    balance - 2 * bet
                    pastNumber = True
                    break
                else:
                    slow_print("You rolled, " + str(newNum) + " the dice will roll again")
            
            slow_print("Your balance is now: " + str(balance))

        print()
        statusLoop = True

        while statusLoop:
            status = input("Do you want to play again? (y/n) ")
            if status == "y":
                statusLoop = False
            elif status == "n":
                gameplay = False
                statusLoop = False
                slow_print("Thanks for playing craps!")
            else:
                clear_terminal()
                slow_print("That is not a valid input.")
        
        if balance <= 0:
            slow_print("You are out of money!")
            gameplay = False

    return balance
