const wheel = {
    0: "Green",
    1: "Black",
    2: "Red",
    3: "Black",
    4: "Black",
    5: "Red",
    6: "Black",
    7: "Red",
    8: "Black",
    9: "Red",
    10: "Black",
    11: "Black",
    12: "Red",
    13: "Black",
    14: "Red",
    15: "Black",
    16: "Red",
    17: "Black",
    18: "Red",
    19: "Red",
    20: "Black",
    21: "Red",
    22: "Black",
    23: "Red",
    24: "Black",
    25: "Red",
    26: "Black",
    27: "Red",
    28: "Black",
    29: "Black",
    30: "Red",
    31: "Black",
    32: "Red",
    33: "Black",
    34: "Red",
    35: "Black",
    36: "Red"
};

const splitNum = [
    [1, 2], [1, 4], [2, 5], [3, 6], [4, 7], [4, 5], [5, 8], [5, 6], [6, 9], 
    [7, 10], [7, 8], [8, 11], [8, 9], [9, 12], [10, 13], [10, 11], [11, 14], 
    [11, 12], [12, 15], [13, 16], [13, 14], [14, 17], [14, 15], [15, 18], 
    [16, 19], [16, 17], [17, 20], [17, 18], [18, 21], [19, 22], [19, 20], 
    [20, 23], [20, 21], [21, 24], [22, 25], [22, 23], [23, 26], [23, 24], 
    [24, 27], [27, 30], [28, 31], [28, 29], [29, 32], [29, 30], [30, 33], 
    [31, 34], [31, 32], [32, 35], [32, 33], [33, 36]
];

const bets = {
    "straight up": 36,
    "split": 18,
    "column": 12,
    "corners": 9,
    "six line bet": 6,
    "row": 3,
    "dozen": 3,
    "odd": 2,
    "even": 2,
    "red": 2,
    "black": 2,
    "low": 2,
    "high": 2
};

function isntInt(rawInput) {
    return isNaN(rawInput);
}

function roulette(balance, betAmount, typeOfBet, specificBet) {
    let win = false;

    if (betAmount > balance) {
        return { error: "Insufficient balance" };
    }

    balance -= betAmount;

    let isInt = false;
    let split, column, corner, SLB, row, dozen, StraightUp;

    if (typeOfBet === "straight up") {
        if (isntInt(specificBet) || specificBet < 0 || specificBet > 36) {
            return { error: "Invalid number for Straight Up bet" };
        }
        StraightUp = parseInt(specificBet);
        isInt = true;
    }

    if (typeOfBet === "split") {
        split = specificBet.split(" ").map(Number).sort();
        if (split.length !== 2 || isntInt(split[0]) || isntInt(split[1]) || !splitNum.some(pair => pair[0] === split[0] && pair[1] === split[1])) {
            return { error: "Invalid numbers for Split bet" };
        }
        isInt = true;
    }

    if (typeOfBet === "column") {
        column = parseInt(specificBet);
        if (isntInt(column) || column % 3 !== 0 || column < 3 || column > 36) {
            return { error: "Invalid number for Column bet" };
        }
        isInt = true;
    }

    if (typeOfBet === "corner") {
        corner = specificBet.split(" ").map(Number);
        if (corner.length !== 4 || corner.some(num => isntInt(num)) || corner[1] - corner[0] !== 3 || corner[1] - corner[2] !== 4 || corner[3] - corner[2] !== 3) {
            return { error: "Invalid numbers for Corner bet" };
        }
        isInt = true;
    }

    if (typeOfBet === "six line bet") {
        SLB = specificBet.split(" ").map(Number);
        if (SLB.length !== 2 || isntInt(SLB[0]) || isntInt(SLB[1]) || Math.abs(SLB[0] - SLB[1]) !== 3 || SLB[0] % 3 !== 0 || SLB[1] % 3 !== 0 || SLB[0] < 3 || SLB[0] > 36 || SLB[1] < 3 || SLB[1] > 36) {
            return { error: "Invalid numbers for Six Line Bet" };
        }
        isInt = true;
    }

    if (typeOfBet === "row") {
        row = specificBet.toLowerCase();
        if (row !== "top" && row !== "middle" && row !== "bottom") {
            return { error: "Invalid row selection" };
        }
        isInt = true;
    }

    if (typeOfBet === "dozen") {
        dozen = specificBet.toLowerCase();
        if (dozen !== "first" && dozen !== "second" && dozen !== "third") {
            return { error: "Invalid dozen selection" };
        }
        isInt = true;
    }

    const value = Math.floor(Math.random() * 37);

    if (typeOfBet === "straight up" && value === StraightUp) win = true;
    if (typeOfBet === "split" && (value === split[0] || value === split[1])) win = true;
    if (typeOfBet === "column" && [column, column + 3, column + 6, column + 9, column + 12].includes(value)) win = true;
    if (typeOfBet === "corner" && corner.includes(value)) win = true;
    if (typeOfBet === "six line bet" && ([...Array(3).keys()].map(i => SLB[0] + i).includes(value) || [...Array(3).keys()].map(i => SLB[1] + i).includes(value))) win = true;
    if (typeOfBet === "row" && ((row === "top" && value % 3 === 0) || (row === "middle" && (value + 1) % 3 === 0) || (row === "bottom" && (value + 2) % 3 === 0))) win = true;
    if (typeOfBet === "dozen" && ((dozen === "first" && value >= 1 && value <= 12) || (dozen === "second" && value >= 13 && value <= 24) || (dozen === "third" && value >= 25 && value <= 36))) win = true;
    if (typeOfBet === "odd" && value !== 0 && value % 2 !== 0) win = true;
    if (typeOfBet === "even" && value % 2 === 0) win = true;
    if ((typeOfBet === "red" || typeOfBet === "black") && wheel[value].toLowerCase() === typeOfBet) win = true;
    if (typeOfBet === "low" && value >= 1 && value <= 18) win = true;
    if (typeOfBet === "high" && value >= 19) win = true;

    if (win) {
        const profit = betAmount * bets[typeOfBet];
        balance += profit;
        return { balance, win: true, profit, value: `${value} ${wheel[value]}` };
    } else {
        return { balance, win: false, value: `${value} ${wheel[value]}` };
    }

    function openForm() {
        document.getElementById("myForm").style.display = "block";
      }
      
    function closeForm() {
        document.getElementById("myForm").style.display = "none";
    }
}
