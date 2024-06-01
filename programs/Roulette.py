# Roulette.py is a python file that runs the back end code for the casino game roulette
# it contains functions that print text slowly, clear the terminal, check if an input is a number, and a list of the wheel
# and the main function where the actual game runs, returning the new balance

import random
import time
import os
from random import randint

wheel = {
    0 : "Green",
    1 : "Black",
    2 : "Red",
    3 : "Black",
    4 : "Black",
    5 : "Red",
    6 : "Black",
    7 : "Red",
    8 : "Black",
    9 : "Red",
    10 : "Black",
    11 : "Black",
    12 : "Red",
    13 : "Black",
    14 : "Red",
    15 : "Black",
    16 : "Red",
    17 : "Black",
    18 : "Red",
    19 : "Red",
    20 : "Black",
    21 : "Red",
    22 : "Black",
    23 : "Red",
    24 : "Black",
    25 : "Red",
    26 : "Black",
    27 : "Red",
    28 : "Black",
    29 : "Black",
    30 : "Red",
    31 : "Black",
    32 : "Red",
    33 : "Black",
    34 : "Red",
    35 : "Black",
    36 : "Red"
}

split_num = [1, 2], [1, 4], [2, 5], [3, 6], [4, 7], [4, 5], [5, 8], [5, 6], [6, 9], [7, 10], [7, 8], [8, 11], [8, 9], [9, 12], [10, 13], [10, 11], [11, 14], [11, 12], [12, 15], [13, 16], [13, 14], [14, 17], [14, 15], [15, 18], [16, 19], [16, 17], [17, 20], [17, 18], [18, 21],  [19, 22], [19, 20], [20, 23], [20, 21], [21, 24], [22, 25], [22, 23], [23, 26], [23, 24], [24, 27], [27, 30], [28, 31], [28, 29], [29, 32], [29, 30], [30, 33], [31, 34], [31, 32], [32, 35], [32, 33], [33, 36]

bets = {
    "straight up" : 36,
    "split" : 18,
    "column" : 12,
    "corners" : 9,
    "six Line Bet" : 6,
    "row" : 3,
    "dozen" : 3,
    "odd" : 2,
    "even" : 2,
    "red" : 2,
    "black" : 2,
    "low" : 2,
    "high" : 2
}

#prints given string slowly
#default delay of 0.1s if no delay peramter is given
def slow_print(input_string, delay=None):
    if delay is None:
        delay = 0.05

    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#clear screen method
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#returns true if input would not be a digit
def isnt_int(raw_inp):
    if(not raw_inp.isdigit()):
        return True

#Main roulette game
def roulette(balance):
    clear_terminal()

    game_over = False
    round_over = False

    #Welcome Statement
    slow_print("Welcome to the Roulette table.")

    while game_over == False:
        
        win = False

        #Setting bet
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

        clear_terminal()

        #Friendly Banter
        if balance == 0:
            slow_print("Wow, we have a real risk taker here!")

        #Initialize type of roulette bet
        slow_print("You have " + str(bet) + " on the line.")
        slow_print("How would you like to bet: ")
        typeOfBet = input('''
        Straight Up, Split, Column, Corners, Six Line Bet, 
        Row,  Dozen, Odd, Even,  Red, Black, Low (1 -18), High (19-36)

        ''').lower()

        placeHolder = True
        while (placeHolder):
            if (bets.get(typeOfBet) == None):
                clear_terminal()
                slow_print("That is not a valid bet")
                typeOfBet = input('''
                Please Choose Again:
                    Straight Up, Split, Column, Corners, Six Line Bet, 
                    Row,  Dozen, Odd, Even,  Red, Black, Low (1 -18), High (19-36)
                                
                ''')
                print()
            else:
                placeHolder = False
        
        clear_terminal()

        #get number for Straight Up bet
        if (typeOfBet == "straight up"):
            isInt = False
            while(isInt == False):
                slow_print("Which number between 0 and 36 would you like to bet on? ")
                Straight_Up = input()
                clear_terminal()
                if isnt_int(Straight_Up):
                    print("That is not a valid roullete number.")
                    print()

                else:
                    Straight_Up = int(Straight_Up)
                    if Straight_Up >= 0 and Straight_Up <= 36:
                        isInt = True

                    else:
                        slow_print("That is not a valid roullete number.")
                        print()

        #get number for Split bet
        if typeOfBet == "split":
            isInt = False
            while(isInt == False):
                slow_print("Which two numbers would you like to bet on that are")
                slow_print("directly next to eachother vertically or horizontally? (EX: '8 11')")
                print('''    3   6   9   12  15  18  21  24  27  30  33  36
    2   5   8   11  14  17  20  23  26  29  32  35
    1   4   7   10  13  16  19  22  25  28  31  34
                    ''')
                split = input().split(" ")
                

                if len(split) != 2:
                    clear_terminal()
                    print("That is not valid. Please enter TWO valid Split numbers.")
                    continue

                if isnt_int(split[0]) or isnt_int(split[1]):
                    clear_terminal()
                    print("Those are not valid Split numbers.")
                    continue

                split[0] = int(split[0])
                split[1] = int(split[1])
                split.sort()
                for i in range(0, (len(split_num) - 1)):
                    if split_num[i][0] == split[0] and split_num[i][1] == split[1]:
                        isInt = True
                        break
                clear_terminal()
                print("Those are not valid Split numbers.")

                
                


        #get number for Column bet
        if typeOfBet == "column":
            isInt = False
            while isInt == False:
                slow_print("Which Column would you like to bet on?")
                slow_print("Use the top numbers as the labels for each column (EX: '9')")
                print('''   '3'   '6'   '9'   '12'  '15'  '18'  '21'  '24'  '27'  '30'  '33'  '36'
    2     5     8     11    14    17    20    23    26    29    32    35
    1     4     7     10    13    16    19    22    25    28    31    34
                    ''')
                column = input()

                cond1 = int(column) % 3 != 0
                cond2 = int(column) <= 3 and int(column) >= 36

                if isnt_int(column):
                    clear_terminal()
                    slow_print("That is not a valid Column bet input.")

                elif cond1 or cond2:
                    clear_terminal()
                    slow_print("That is not a valid Column bet input.")
                
                else:
                    column = int(column)
                    isInt = True
                    clear_terminal()

        if typeOfBet == "corner":
            isInt = False
            while isInt == False:
                slow_print("Which 4 numbers would you like to bet on that form a square on the betting table?")
                slow_print("Enter them in order they show up on the board. (EX: '8 11 7 10')")
                print('''3   6   9   12  15  18  21  24  27  30  33  36
    2   5   8   11  14  17  20  23  26  29  32  35
    1   4   7   10  13  16  19  22  25  28  31  34''')
                corner = input().split()

                if isnt_int(corner[0]) or isnt_int(corner[1]) or isnt_int(corner[2]) or isnt_int(corner[3]):
                    clear_terminal()
                    slow_print("Please enter valid roulette numbers.")
                
                elif int(corner[1]) - int(corner[0]) != 3 or int(corner[1]) - int(corner[2]) != 4 or int(corner[3]) - int(corner[2]) != 3:
                    clear_terminal()
                    slow_print("Please enter valid roulette numbers.")

                else:
                    isInt = True
                

        #get numbers for Six Line Bet
        if typeOfBet == "six line bet":
            isInt = False
            while isInt == False:
                slow_print("Which two lines would you like to bet on?")
                slow_print("Use the top numbers as the labels for each line and make sure they lines are next to eachother? (EX: '12 15')")
                print('''   '3'   '6'   '9'   '12'  '15'  '18'  '21'  '24'  '27'  '30'  '33'  '36'
    2     5     8     11    14    17    20    23    26    29    32    35
    1     4     7     10    13    16    19    22    25    28    31    34
                    ''')
                SLB = input().split()

                cond1 = abs(int(SLB[0]) - int(SLB[1])) != 3
                cond2 = int(SLB[0]) % 3 != 0
                cond3 = int(SLB[1]) % 3 != 0
                cond4 = int(SLB[0]) >= 3 and int(SLB[0]) <= 36
                cond5 = int(SLB[1]) >= 3 and int(SLB[1]) <= 36

                if len(SLB) > 2 or cond1 or cond2 or cond3 or cond4 or cond5 or isnt_int(SLB[0]) or isnt_int(SLB[1]):
                    clear_terminal()
                    slow_print("That is not a valid Six-Line bet input.")
                
                else:
                    isInt = True

        if typeOfBet == "row":
            isInt = False
            while isInt == False:
                slow_print("Which row would you like to bet on? (Top, Bottom, or Middle)")
                print('''3   6   9   12  15  18  21  24  27  30  33  36
    2   5   8   11  14  17  20  23  26  29  32  35
    1   4   7   10  13  16  19  22  25  28  31  34''')
                row = input().lower()
                
                if row != "top" and row != "middle" and row != "bottom":
                    clear_terminal()
                    slow_print("That is not a valid Row bet.")
            
                else:
                    isInt = True

        #get number for Dozen bet
        if typeOfBet == "dozen":
            isInt = False
            while isInt == False:
                slow_print("Which Dozen set would you like to bet on: ")
                slow_print("Please enter either 'First' (1-12), 'Second' (13-24), or 'Third' (24-36)")
                dozen = input().lower()

                if dozen != "first" and dozen != "second" and dozen != "third":
                    clear_terminal()
                    print("That is not a valid dozen bet.")
                
                else:
                    isInt = True
                    

        #roullete wheel simulation
        clear_terminal()
        slow_print("Alright, betting " + typeOfBet)
        slow_print( "Time to Roll")
        print()
        slow_print("Rolling... Rolling... Rolling... ", 0.2)
        clear_terminal()
        value = randint(0, 37)
        slow_print(str(value) + " " + str(wheel[value]))
        print()
        
        #Results for Straight Up bet
        if typeOfBet == "straight Up":
            if value == Straight_Up:
                win = True

        #Results for Split bet
        if typeOfBet == "split":
            if value == int(split[0]) or value == int(split[1]):
                win = True

        #Results for Column Bet
        if typeOfBet == "column":
            for i in 3:
                if (column + i) == value:
                    win = True
                    break

        if typeOfBet == "corner":
            for i in corner:
                if int(i) == value:
                    win = True
                    break

        #Results for Six Line Bet
        if typeOfBet == "six line bet":
            for i in SLB:
                for x in range(3):
                    if (int(i) + x) == value:
                        win = True
                        break

        #Results for Row bet
        if typeOfBet == "row":
            if row == "top" and value % 3 == 0:
                win = True
            elif row == "middle" and (value + 1) % 3 == 0:
                win = True
            elif row == "bottom" and (value + 2) % 3 == 0:
                win = True

        #Results for Dozen bet
        if typeOfBet == "dozen":
            if value >= 13 and value <= 24 and dozen == "second":
                win = True
            elif value >= 1 and value <= 12 and dozen == "first":
                win = True
            elif value >= 25 and dozen == "third":
                win = True

        #Results for Odd bet
        if typeOfBet == "odd":
            if value != 0:
                if value % 2 != 0:
                    win = True
        
        #Results for Even bet
        if typeOfBet == "even":
            if value % 2 == 0:
                win = True

        #Results for Red or Black bet
        if wheel[value] == typeOfBet:
                win = True

        #Results for Low bet
        if typeOfBet == "low":
            if value >= 1 and value <= 18:
                win = True

        #Results for High bet
        if typeOfBet == "high":
            if value >= 19:
                win = True

        #Results for win
        if win:
            profit = (bet * bets.get(typeOfBet))
            balance += profit
            slow_print("You won " + str(profit) + ", your balance is now " + str(balance) + "!")
        
        #Results for loss
        if win == False:
            if balance <= 0:
                slow_print("Better luck next time, you're out of money bud.")
                game_over = True
                break
            else:
                slow_print("Tough luck, house wins. You still have " + str(balance) + " left in your balance.", 0.05)

        #Play again? prompt
        slow_print("Would you like to play again? Y or N ")\
        
        if input().lower() == "n":
            clear_terminal()
            slow_print("Okay, hope to see you soon!")
            break
        else:
            clear_terminal()
            slow_print("Great choice!")

    return balance
