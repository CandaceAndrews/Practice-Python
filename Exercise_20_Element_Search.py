# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

# -------

def inside_list(list, number):
    for element in list:
        if element == number:
            return True
    return False


if __name__ == "__main__":
    test_list = [0, 1, 2, 3, 4, 5, 7, 8, 9]
    print(inside_list(test_list, 5))


inside_list(test_list, 9)
