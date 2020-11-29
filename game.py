import random

def main():
    player1 = 0
    player2 = 0
    rounds = 1

    while rounds!=4:
        print("\nRound " +str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll =" +str(player1))
        print("Player 2 Roll =" +str(player2))

        if player1 == player2:
            print("Draw")
        elif player1>player2:
            print("player 1 Wins!")
        else:
            print("player 2 wins!") 
        rounds = rounds + 1 

def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()

