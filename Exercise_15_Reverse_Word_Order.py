# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

# -------

def reverse_sentence():
    string = input("Please enter sentence to reverse:   ")
    new_string = string.split(" ")
    reverse_string = ' '.join(new_string[::-1])
    print(reverse_string)


reverse_sentence()
