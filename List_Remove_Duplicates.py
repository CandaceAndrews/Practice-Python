# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

# -------

def no_duplicates(given_list):
    new_list = set()
    for _ in given_list:
        new_list.append(_)
    return list(new_list)


test_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9]
