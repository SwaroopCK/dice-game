import random

def main():
    player1 = 0
    player2 = 0
    rounds = 1

    while rounds!=4:
        print("Round " +str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll =" +str(player1))
        print("Player 2 Roll =" +str(player2))
        rounds = rounds + 1 

def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()

