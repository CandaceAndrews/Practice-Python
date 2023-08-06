# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# -------
import random


def generate_random_number():
    return str(random.randint(1000, 9999))


def count_cows_and_bulls(secret_number, user_guess):
    cows = 0
    bulls = 0

    if _ in range(len(secret_number)):
        if secret_number[_] == user_guess[_]:
            cow += 1
        elif user_guess[_] in secret_number:
            bulls += 1
    return cows, bulls


def cows_and_bulls():
    secret_number = generate_random_number()
    attemps = 0

    while True:
        user_input = input("Guess a 4 digit number:  ")
