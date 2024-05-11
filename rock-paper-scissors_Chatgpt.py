import random

def get_player_move():
    while True:
        move = input("Choose your move (R for Rock, P for Paper, S for Scissors): ").lower()
        if move in ["r", "p", "s"]:
            if move == "r":
                return "rock"
            elif move == "p":
                return "paper"
            else:
                return "scissors"
        else:
            print("Invalid input. Please enter 'R', 'P', or 'S'.")

def get_pc_move(options):
    return random.choice(options)

def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie"
    elif (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "rock" and player2 == "scissors"):
        return "You Win!"
    else:
        return "You Lost!"

options = ["rock", "paper", "scissors"]

print("Game Started")

while True:
    player1 = get_player_move()
    player2 = get_pc_move(options)

    print(f"You Entered {player1}, PC Entered {player2}")

    print(determine_winner(player1, player2))
