# Character Input --
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# -------

name = input("What is your name? ")
age = int(input("What is your age? "))
year = 2023 - age + 100

print(f"In {year}, {name} will be 100 years old!!")
