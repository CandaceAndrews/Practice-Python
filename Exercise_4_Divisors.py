# Exercise 4
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# -------

chosen_number = int(
    input("Please select a number to see the divisors for that number:  "))

range_to_number = list(range(1, chosen_number + 1))

divisor_list = []

for number in range_to_number:
    if chosen_number % number == 0:
        divisor_list.append(number)


for spot in divisor_list:
    print(spot)
