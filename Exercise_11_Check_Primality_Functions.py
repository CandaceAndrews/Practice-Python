# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).

# -------

number = int(input("Please select a number:  "))

divisors_of_number = [x for x in range(2, number) if number % x == 0]


def prime_or_not(num):
    if number > 1:
        if len(divisors_of_number) == 0:
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")


prime_or_not(number)
