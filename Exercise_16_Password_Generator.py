# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
# of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your run-time code in a main method.

# -------
import random
import string


def password_generator():
    short_password = []
    medium_password = []
    strong_password = []

    alphabet_lower = [a, b, c, d, e, f, ]

    user_request = input(
        "Please choose password type:  Short, Medium or Strong:   ")
