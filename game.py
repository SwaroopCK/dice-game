import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds!=6:
        print("\nRound " +str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll =" +str(player1))
        print("Player 2 Roll =" +str(player2))

        if player1 == player2:
            print("Draw")
        elif player1>player2:
            player1wins = player1wins + 1
            print("player 1 Wins!")
        else:
            player2wins = player2wins + 1
            print("player 2 wins!") 
        rounds = rounds + 1 

    if player1wins == player2wins:
        print("\nDraw match")
    elif player1wins > player2wins:
        print("\nPlayer 1 win the game by "+ str(player1wins)+" rounds")
    else:
        print("\nPlayer 2 win the game by "+ str(player2wins)+" rounds")

def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()

