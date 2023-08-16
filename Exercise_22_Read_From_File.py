# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen.

# -------

counting_names_dict = {}

with open('file_to_read.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counting_names_dict:
            counting_names_dict[line] += 1
        else:
            counting_names_dict[line] = 1
        line = f.readline()

print(counting_names_dict)
