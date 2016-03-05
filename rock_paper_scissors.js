var win = function(player_move, computer_move)
{
    var check = convert(player_move) - convert(computer_move);
    console.log("check is %d", check);
    if (check === 0)
        console.log("Tie");
    else if (check === -1 || check === 2)
        console.log("Player won!");
    else
        console.log("Computer won!");
};

var convert = function(move)
{
    if (move === "rock")
        return 0;
    else if (move === "scissors")
        return 1;
    else if (move === "paper")
        return 2;
    else
        console.log("Invalid move!");
        return null;
};

var computerMove = function(number)
{
    if (0 <= number <= 0.33)
        return "rock";
    else if (0.34 <= number <= 0.66)
        return "paper";
    else
        return "scissors";
};

var userChoice = prompt("Your move?");
var computerChoice = computerMove(Math.random());
console.log(computerChoice);
win(userChoice, computerChoice);