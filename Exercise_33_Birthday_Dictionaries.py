# For this exercise, we will keep track of when our friend’s birthdays are, and be able
# to find that information based on their name. Create a dictionary (in your file) of names
# and birthdays. When you run your program it should ask the user to enter a name, and return
# the birthday of that person back to them.

# -------

birthday_dict = {
    "Claire Redfield": "Oct. 17th, 1987",
    "Leon Kennedy": "Sept. 24th, 1985",
    "Sherry Birkin": "Nov. 11th, 1999",
}


def find_birthday():
    birthday_to_find = input("Who's birthday do you want to look up?")
