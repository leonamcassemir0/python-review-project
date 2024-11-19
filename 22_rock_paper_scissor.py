def rpsWinner(player1, player2):
    if player1 == 'rock' and player2 == 'scissors':
        return 'player1'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'player1'
    elif player1 == 'paper' and player2 == 'rock':
        return 'player1'
    elif player1 == player2:
        return 'tie'
    else:
        return 'player2'


print(rpsWinner('rock', 'paper'))
print(rpsWinner('rock', 'scissors'))
print(rpsWinner('paper', 'scissors'))
print(rpsWinner('paper', 'rock'))
print(rpsWinner('scissors', 'rock'))
print(rpsWinner('scissors', 'paper'))
print(rpsWinner('rock', 'rock'))
print(rpsWinner('paper', 'paper'))
print(rpsWinner('scissors', 'scissors'))
