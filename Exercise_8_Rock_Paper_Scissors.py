import random
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

#  -------

def paper_rock_scissors_game(decision):
    quit_game = "No"
    options = ["paper", "rock", "scissors"]
    player_choice = input("Please Choose: Paper, Rock or Scissors").lower()
    computer_choice = random.choice(options).lower()
    
    while quit_game != "exit":
        if player_choice == "paper" and 