/* 
Craps JavaScript file that returns the winnings or losings of the user.
Rolls two dice until it meets the requirments.
*/

function Craps_Roll(Balance, Bet, bet_type, OldNumber) {
    const roll = Dice_roll();
    number = roll[0] + roll[1]
    const result = [Balance, "non", roll[1], roll[2]];
    if (bet_type == "PassLineBet") {
        if (number != null) {
            if ((number) == OldNumber) {
                Balance = Balance + Bet;
                result[1] == "win"
                return result;
            } 
            else if ((roll[0] + roll[1]) == 7) {
                result[1] == "lose";
                Balance = Balance - Bet;
                return result;
            }
            else {
                result[2] = (roll[0] + roll[1]);
                return result;
            }
        }
        if ((roll[0] + roll[1]) == 7 || (roll[0] + roll[1]) == 11){
            result = Balance + Bet;
            result[1] == "win"
            return result;
        }
        else if ((roll[0] + roll[1]) == 2 || (roll[0] + roll[1]) == 3 || (roll[0] + roll[1]) == 12) {
            result = Balance - Bet;
            result[1] == "lose"
            return result;
        }
    }

        if (bet_type == "DontPassBet") {
            if (number != null) {
                if (number == OldNumber) {
                    result = Balance - Bet;
                    result[1] == "lose"
                    return result;
                } 
                else if ((roll[0] + roll[1]) == 7) {
                    result = Balance + Bet;
                    result[1] == "win"
                    return result;
                }
                else {
                    result = Balance;
                    return result;
                }
            }
            if ((roll[0] + roll[1]) == 2 || (roll[0] + roll[1]) == 3){
                result = Balance + Bet;
                result[1] == "win"
                return result;
            }
            else if ((roll[0] + roll[1]) == 7 || (roll[0] + roll[1]) == 11) {
                result = Balance - Bet;
                result[1] == "lose"
                return result;
            }
        }
    

    } 

function Dice_roll() {
    const results = [Math.floor(Math.random(1, 6)), Math.floor(Math.random(1, 6))];
    return results;
}
