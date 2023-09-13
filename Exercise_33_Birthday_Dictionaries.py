# For this exercise, we will keep track of when our friend’s birthdays are, and be able
# to find that information based on their name. Create a dictionary (in your file) of names
# and birthdays. When you run your program it should ask the user to enter a name, and return
# the birthday of that person back to them.

# -------

if __name__ == '__main__':

    birthdays = {
        'Leon': '03/14/1985',
        'Claire': '01/17/1987',
        'Ada': '12/10/1986',
        'Sherry': '06/14/1999',
        'Kendo': '01/6/1968'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    name = input('Who\'s birthday do you want to look up? ')

    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}")
