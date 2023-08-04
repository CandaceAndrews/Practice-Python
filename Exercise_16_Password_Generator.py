# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
# of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your run-time code in a main method.

# -------
import random
import string


def password_generator():

    symbols = "!@#$%^&*?"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits

    full_password_bank = symbols + lowercase + uppercase + numbers

    user_request = input(
        "Please choose password type:  Short, Medium or Strong:   ").lower()

    if user_request == "short":
        short_password = ''.join(
            [random.choice(full_password_bank) for _ in range(5)])
        print(short_password)
    elif user_request == "medium":
        medium_password = ''.join(
            [random.choice(full_password_bank) for _ in range(7)])
        print(medium_password)
    elif user_request == "strong":
        strong_password = ''.join(
            [random.choice(full_password_bank) for _ in range(9)])
        print(strong_password)
    else:
        print("Please input valid response.")


password_generator()
