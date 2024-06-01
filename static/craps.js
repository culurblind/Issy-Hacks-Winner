function Craps_Roll(Balance, Bet, bet_type, OldNumber) {
    const roll = Dice_roll();
    const number = roll[0] + roll[1];
    let result = [Balance, "none", roll[0], roll[1]];

    if (bet_type === "PassLineBet") {
        if (OldNumber != null) {
            if (number === OldNumber) {
                Balance += Bet;
                result[1] = "win";
                result[0] = Balance;
                return result;
            } else if (number === 7) {
                Balance -= Bet;
                result[1] = "lose";
                result[0] = Balance;
                return result;
            } else {
                return result;
            }
        }
        if (number === 7 || number === 11) {
            Balance += Bet;
            result[1] = "win";
            result[0] = Balance;
            return result;
        } else if (number === 2 || number === 3 || number === 12) {
            Balance -= Bet;
            result[1] = "lose";
            result[0] = Balance;
            return result;
        }
    }

    if (bet_type === "DontPassBet") {
        if (OldNumber != null) {
            if (number === OldNumber) {
                Balance -= Bet;
                result[1] = "lose";
                result[0] = Balance;
                return result;
            } else if (number === 7) {
                Balance += Bet;
                result[1] = "win";
                result[0] = Balance;
                return result;
            } else {
                return result;
            }
        }
        if (number === 2 || number === 3) {
            Balance += Bet;
            result[1] = "win";
            result[0] = Balance;
            return result;
        } else if (number === 7 || number === 11) {
            Balance -= Bet;
            result[1] = "lose";
            result[0] = Balance;
            return result;
        }
    }

    return result;
}

function Dice_roll() {
    const results = [Math.floor(Math.random() * 6) + 1, Math.floor(Math.random() * 6) + 1];
    return results;
}
