# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

# -------

def inside_list(list, number):
    if number in list:
        print("True")
    else:
        print("False")


test_list = [0, 1, 2, 3, 4, 5, 7, 8, 9]

inside_list(test_list, 9)

# -------

def binary_search(list, number):
    