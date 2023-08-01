# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

# -------

def list_ends(user_input_list):
    if len(user_input_list) < 2:
        return "List should contain at least two elements."
    first = user_input_list[0]
    last = user_input_list[-1]
    return [first, last]


a = [5, 10, 15, 20, 25]
result = list_ends(a)
print(result)
