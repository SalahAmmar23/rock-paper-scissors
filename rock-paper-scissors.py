import random

# we will start beginner steps to make rock-paper-scissors game 
#Options we got 
options = ["rock", "paper", "scissors"]

print("Game Started")

while True:
    player1 = input("Choose your move Rock, Paper, Scissors: ").lower()
    player2 = random.choice(options)

    print(f"You Entered {player1} ,Pc Entered {player2}")

    if  player1 == player2 :
        print("It's A tie")
            
    elif (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "scissors") :
        print("You Win!")
            
    elif player1 not in options:
        print("You Need to type one of the following : Rock, Paper, Scissors") 

    else: 
        print("You Lost!")