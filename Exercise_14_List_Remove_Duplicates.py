# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

# -------

test_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9]

# function using sets


def no_duplicates_set(given_list):
    new_set = set(given_list)
    new_list = list(new_set)
    print(new_list)


no_duplicates_set(test_list)


# function using loop
def no_duplicates_loop(given_list):
    new_list = []
    for _ in given_list:
        if _ not in new_list:
            new_list.append(_)
    print(new_list)


no_duplicates_loop(test_list)
