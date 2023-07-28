import random
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

#  -------


def paper_rock_scissors_game():
    game_in_progress = True
    options = ["paper", "rock", "scissors"]
    player_choice = input("Please Choose: Paper, Rock or Scissors:  ").lower()
    computer_choice = random.choice(options).lower()

    lose = "You Lose!"
    win = "You win!"

    while game_in_progress:
        if player_choice == computer_choice:
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print("Tie!")
            break
        elif player_choice == "paper" and computer_choice == "rock":
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print(win)
            break
        elif player_choice == "paper" and computer_choice == "scissors":
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print(lose)
            break
        elif player_choice == "rock" and computer_choice == "paper":
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print(lose)
            break
        elif player_choice == "rock" and computer_choice == "scissors":
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print(win)
            break
        elif player_choice == "scissors" and computer_choice == "paper":
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print(win)
            break
        elif player_choice == "scissors" and computer_choice == "rock":
            print(f"Player: {player_choice}")
            print(f"Computer: {computer_choice}")
            print(lose)
            break
        else:
            print("Please input valid response!")

    play_again = input("Play again? Yes or No:  ").lower()
    if play_again == "yes":
        paper_rock_scissors_game()


paper_rock_scissors_game()
