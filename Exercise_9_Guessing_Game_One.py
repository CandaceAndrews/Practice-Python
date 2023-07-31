# Exercise 9 (and Solution)
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# -------
import random


def number_guessing_game():

    computer_number = random.randint(1, 9)
    player_number = 0
    while player_number != computer_number:
        player_number = int(input("Please select a number from 1 to 9:  "))

        if player_number not in range(1, 10):
            print("Out of range!")
        elif player_number < computer_number:
            print(f"{player_number} is too low!")
        elif player_number > computer_number:
            print(f"{player_number} is too high")
        else:
            print(f"Correct!!\nComputer's Number: {computer_number}")
            break

    play_again = input("Play Again: Yes or No:  ").lower()

    if play_again == "yes":
        number_guessing_game()


number_guessing_game()
