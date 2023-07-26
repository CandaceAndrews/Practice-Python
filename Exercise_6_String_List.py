# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# -------

user_input = input("Please enter a word: ")


def palindrome_check(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        print("Is a Palindrome!")
    else:
        print("Is not a Palindrome.")


palindrome_check(user_input)
