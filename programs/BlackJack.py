# BlackJack.py is a python file that runs the back end code for the casino game black jack
# it contains functions that print text slowly, clear the terminal, check if an input is a number, and a list of the cards associated with values 
# and the main function where the actual game runs, returning the new balance

# import statements
import random
import time
import os

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

# All the cards
cards = {
    "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11
}
cardKeys = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def blackJack(balance):
    clear_terminal()
    slow_print("Welcome to Black Jack!")
    time.sleep(0.5)

    # game runs while balance is more than 0
    while balance > 0:
        time.sleep(2)
        clear_terminal()
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

        # player hand
        print()
        playerHand = []
        card1 = cardKeys[random.randint(0, 12)]
        card2 = cardKeys[random.randint(0, 12)]
        playerHand.append(card1)
        playerHand.append(card2)
        card1Val = cards.get(card1)
        card2Val = cards.get(card2)
        sum = card1Val + card2Val
        slow_print("Player Card: " + card1)
        slow_print("Player Card: " + card2)
        # double ace case
        if card1 == "A" and card2 == "A":
            sum -= 10
            playerHand.remove("A")
        slow_print("total = " + str(sum))
        time.sleep(1)

        # dealer hand
        print()
        dealerHand = []
        dealerCard = cardKeys[random.randint(0, 12)]
        dealerHand.append(dealerCard)
        dealerCard1Val = cards.get(dealerCard)
        dealerSum = dealerCard1Val
        slow_print("Dealer Card: " + dealerCard)

        turn = False

        # case 1 - black jack
        if sum == 21:
            print()
            slow_print("Black Jack!")
            # dealer card reveal
            while dealerSum < 17:
                dealerExtraCard = cardKeys[random.randint(0, 12)]
                dealerHand.append(dealerExtraCard)
                dealerExtraCardVal = cards.get(dealerExtraCard)
                dealerSum += dealerExtraCardVal
                slow_print("Dealer Card: " + dealerExtraCard)
                slow_print("Dealer total = " + str(dealerSum))
                if "A" in dealerHand and dealerSum > 21:
                    dealerSum -= 10
                    dealerHand.remove("A")
                time.sleep(0.5)
            # conditionala to determine win, loss, or tie
            if dealerSum > 21:
                slow_print("Dealer Bust")
                balance += 2.5 * bet
                balance = int(balance)
            elif dealerSum == 21:
                slow_print("Push")
                balance += bet
            else:
                balance += 2.5 * bet
                balance = int(balance)
        else:
            # if it is not a black jack give the options
            turn = True
            hit = False

        while turn:
            print()
            decision = input("stand, hit, double, or split? ")
            print()

            # case 2 - stand
            if decision == "stand":
                # dealer card reveal
                while dealerSum < 17:
                    dealerExtraCard = cardKeys[random.randint(0, 12)]
                    dealerHand.append(dealerExtraCard)
                    dealerExtraCardVal = cards.get(dealerExtraCard)
                    dealerSum += dealerExtraCardVal
                    slow_print("dealer's card: " + str(dealerExtraCard))
                    if "A" in dealerHand and dealerSum > 21:
                        dealerSum -= 10
                        dealerHand.remove("A")
                    slow_print("Dealer total = " + str(dealerSum))
                    time.sleep(0.5)
                # conditionals to determine winner
                if dealerSum > 21:
                    slow_print("Dealer Bust")
                    balance += 2 * bet
                elif dealerSum == sum:
                    slow_print("Push")
                    balance += bet
                elif dealerSum < sum:
                    slow_print("You Win!")
                    balance += 2 * bet
                elif dealerSum > sum:
                    slow_print("Dealer Wins")
                turn = False

            # case 2 - hit
            elif decision == "hit":
                # creating an additional card and append it to the player's hand
                extraCard = cardKeys[random.randint(0, 12)]
                playerHand.append(extraCard)
                slow_print("Player Card: " + extraCard)
                extraCardVal = cards.get(extraCard)
                sum += extraCardVal
                # conditionals if the hit makes the total 21 or greater
                if sum > 21:
                    if "A" in playerHand:
                        sum -= 10
                        playerHand.remove("A")
                    else:
                        slow_print("bust")
                        turn = False
                slow_print("total = " + str(sum))
                if sum == 21:
                    dealerCard = cardKeys[random.randint(0, 12)]
                    dealerHand.append(dealerCard)
                    dealerCardVal = cards.get(dealerCard)
                    slow_print("dealer's card: " + str(dealerCard))
                    dealerSum += dealerCardVal
                    slow_print("dealer total: " + str(dealerCardVal))
                    if dealerCard == 21:
                        slow_print("push")
                        balance += bet
                    else:
                        slow_print("you win")
                        balance += 2*bet
                        balance = int(balance)
                    turn = False
                hit = True
            
            # case 3 - double (only if us have enough to double)
            elif decision == "double":
                balance -= bet
                # conditional to make sure player has enough money to double
                if balance < 0:
                    slow_print("don't have the money to double")
                    balance += bet
                elif hit:
                    slow_print("you already hit you cannot double now")
                else:
                    bet *= 2
                    slow_print(balance)
                    print()
                    # one extra card for the double
                    extraCard = cardKeys[random.randint(0, 12)]
                    slow_print("Player Card: " + extraCard)
                    playerHand.append(extraCard)
                    extraCardVal = cards.get(extraCard)
                    sum += extraCardVal
                    time.sleep(0.25)
                    switch = True
                    if sum > 21:
                        if "A" in playerHand:
                            sum -= 10
                            playerHand.remove("A")
                        else:
                            slow_print("bust")
                            turn = False
                            switch = False
                    slow_print("total = " + str(sum))
                    print()
                    # if no bust then run this code
                    if switch:
                        # dealer card reveal
                        while dealerSum < 17:
                            dealerExtraCard = cardKeys[random.randint(0, 12)]
                            dealerHand.append(dealerExtraCard)
                            dealerExtraCardVal = cards.get(dealerExtraCard)
                            dealerSum += dealerExtraCardVal
                            slow_print("dealer's card: " + str(dealerExtraCard))
                            if "A" in dealerHand and dealerSum > 21:
                                dealerSum -= 10
                                dealerHand.remove("A")
                            slow_print("Dealer total = " + str(dealerSum))
                            time.sleep(0.5)
                        # conditionals to determine winner
                        if dealerSum > 21:
                            slow_print("dealer bust")
                            balance += 2*bet
                        elif dealerSum > sum:
                            slow_print("dealer won")
                        elif dealerSum < sum:
                            slow_print("you win")
                            balance += 2*bet
                        else:
                            slow_print("push")
                            balance += bet
                        turn = False        
            
            #case 4 - split
            elif decision == "split":
                if hit:
                    slow_print("you already hit you cannot double now")
                # runs code only if the 2 cards are the same value
                elif card1Val == card2Val:
                    balance -= bet
                    # won't run split if the money is not enough
                    if balance < 0:
                        slow_print("don't have the money to split")
                        balance += bet
                    else:
                        # getting the other cards for each split
                        slow_print("balance: " + str(balance))
                        print()
                        splitHand1 = []
                        splitHand2 = []
                        splitHand1.append(card1)
                        splitHand2.append(card2)
                        
                        splitCard1 = cardKeys[random.randint(0, 12)]
                        splitHand1.append(splitCard1)
                        splitCard1Val = cards.get(splitCard1)
                        sum1 = card1Val + splitCard1Val

                        splitCard2 = cardKeys[random.randint(0, 12)]
                        splitHand2.append(splitCard2)
                        splitCard2Val = cards.get(splitCard2)
                        sum2 = card2Val + splitCard2Val

                        slow_print("first split: " + splitCard1)
                        slow_print("first split total: " + str(sum1))
                        print()
                        slow_print("second split: " + splitCard2)
                        slow_print("first split total: " + str(sum2))
                        print()

                        splitTurn1 = True
                        splitTurn2 = False
                        dealerReveal = False

                        # first split hit and stand
                        while (splitTurn1):
                            if sum1 == 21:
                                dealerReveal = True
                                splitTurn1 = False
                                splitTurn2 = True
                            elif sum1 > 21:
                                slow_print("split 1 busts")
                                splitTurn1 = False
                                splitTurn2 = True
                            else:
                                splitDecision = input("Split 1: hit or stand? ")
                                if splitDecision == "hit":
                                    extraCard1 = cardKeys[random.randint(0, 12)]
                                    splitHand1.append(extraCard1)
                                    extraCard1Val = cards.get(extraCard1)
                                    sum1 += extraCard1Val
                                    slow_print("split 1 card: " + extraCard1)
                                    if sum1 > 21:
                                        if "A" in splitHand1:
                                            sum -= 10
                                            playerHand.remove("A")
                                        else:
                                            slow_print("split 1 busts")
                                            splitTurn1 = False
                                            splitTurn2 = True
                                    slow_print("split 1 total = " + str(sum1))
                                    if sum1 == 21:
                                        dealerReveal = True
                                        splitTurn1 = False
                                        splitCard2 = True

                                elif splitDecision == "stand":
                                    dealerReveal = True
                                    splitTurn1 = False
                                    splitTurn2 = True
                            
                            print()

                            # second split hit or stand
                            while (splitTurn2):
                                if sum2 == 21:
                                    dealerReveal = True
                                    splitTurn2 = False
                                elif sum2 > 21:
                                    slow_print("split 2 busts")
                                    splitTurn2 = False
                                else:
                                    splitDecision = input("Split 2: hit or stand? ")
                                    if splitDecision == "hit":
                                        extraCard2 = cardKeys[random.randint(0, 12)]
                                        splitHand2.append(extraCard2)
                                        extraCard2Val = cards.get(extraCard2)
                                        sum2 += extraCard2Val
                                        slow_print("split 2 card: " + extraCard2)
                                        if sum2 > 21:
                                            if "A" in splitHand2:
                                                sum -= 10
                                                playerHand.remove("A")
                                            else:
                                                slow_print("split 2 busts")
                                                splitTurn2 = False
                                        slow_print("split 2 total = " + str(sum2))
                                        if sum2 == 21:
                                            dealerReveal = True
                                            splitCard2 = False
                                    elif splitDecision == "stand":
                                        dealerReveal = True
                                        splitTurn2 = False
                            
                            # dealer card reveal
                            if (dealerReveal):
                                while dealerSum < 17:
                                    dealerExtraCard = cardKeys[random.randint(0, 12)]
                                    dealerHand.append(dealerExtraCard)
                                    dealerExtraCardVal = cards.get(dealerExtraCard)
                                    dealerSum += dealerExtraCardVal
                                    print()
                                    slow_print("dealer's card: " + str(dealerCard))
                                    if "A" in dealerHand and dealerSum > 21:
                                        dealerSum -= 10
                                        dealerHand.remove("A")
                                    slow_print("Dealer total = " + str(dealerSum))
                                    time.sleep(0.5)

                                # determine winner
                                if dealerSum > 21:
                                    slow_print("Dealer Bust!")
                                    if sum1 <= 21:
                                        balance += bet
                                    if sum2 <= 21:
                                        balance += 2*bet
                                else:
                                    if dealerSum > sum1:
                                        slow_print("first split loses")
                                    elif dealerSum < sum1:
                                        slow_print("first split wins")
                                        balance += 2*bet
                                    else:
                                        slow_print("first split pushes")
                                        balance += bet

                                    if dealerSum > sum2:
                                        slow_print("second split loses")
                                    elif dealerSum < sum2:
                                        slow_print("second split wins")
                                        balance += 2*bet
                                    else:
                                        slow_print("second split pushes")
                                        balance += bet

                            turn = False
                else:
                    slow_print("your cards are not the same, you can not split")
        
        print()
        status = input("Do you want to play again? (y/n) ")
        statusLoop = True

        while statusLoop:
            if status == "y":
                statusLoop = False
            elif status == "n":
                statusLoop = False
                slow_print("Thanks for playing BlackJack!")
                return balance
            else:
                slow_print("Type y or n")

    if balance <= 0:
        slow_print("You are out of money!")

    return balance
