# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).

# -------

number = int(input("Please select a number:  "))

answer = [x for x in range(2, number) if number % x == 0]

print(answer)
