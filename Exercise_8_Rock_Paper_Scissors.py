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
    quit_game = "No"
    options = ["paper", "rock", "scissors"]
    player_choice = input("Please Choose: Paper, Rock or Scissors:  ").lower()
    computer_choice = random.choice(options).lower()

    lose = "You Lose!"
    win = "You win!"

    while quit_game != "yes":
        if player_choice == computer_choice:
            print(computer_choice)
            print("Tie!")
            quit_game = input("Keep playing? Yes or No:  ").lower
        elif player_choice == "paper" and computer_choice == "rock":
            print(computer_choice)
            print(win)
            quit_game = input("Keep playing? Yes or No:  ").lower
        elif player_choice == "paper" and computer_choice == "scissors":
            print(computer_choice)
            print(lose)
            quit_game = input("Keep playing? Yes or No:  ").lower
        elif player_choice == "rock" and computer_choice == "paper":
            print(computer_choice)
            print(lose)
            quit_game = input("Keep playing? Yes or No:  ").lower
        elif player_choice == "rock" and computer_choice == "scissors":
            print(computer_choice)
            print(win)
            quit_game = input("Keep playing? Yes or No:  ").lower
        elif player_choice == "scissors" and computer_choice == "paper":
            print(computer_choice)
            print(win)
            quit_game = input("Keep playing? Yes or No:  ").lower
        elif player_choice == "scissors" and computer_choice == "rock":
            print(computer_choice)
            print(lose)
            quit_game = input("Keep playing? Yes or No:  ").lower
        else:
            print("Please input valid response!")


paper_rock_scissors_game()
