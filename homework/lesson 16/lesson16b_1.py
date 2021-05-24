# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson16b_1.py
# Description: Write a program which takes a list of names from the user
# prints all elements in the list that start with “P”.
# Modify your program so the user can specify the starting letter.
# Modify your program so you print any string which contains a numeric digit.
#
# *****************************************************

# variable declaration
names = []  # list for names
amount = int()  # amount of names wanted to input

# input: prompting user for the number of names they want to input
amount = int(input("How many names would you like to input?: "))

# input: prompting user for the names
for i in range(amount):
    names.append(input("Please enter a name: "))

# process: changing all the characters to lowercase
for i in range(len(names)):
    names[i] = names[i].lower()

# printing the names with p as the start
print(f"the names that start with p are:")
for i in names:
    if i.startswith('p'):  # using a startswith function
        print(i, end=" ")


# modification part:
print()
print("<<<PART MODIFICATION>>>")

# variable declaration
names = []
amount = int()

# input: prompting user for number of names and names
amount = int(input("How many names would you like to input?: "))
for i in range(amount):
    names.append(input("Please enter a name: "))

# changing all characters to lowercase
for i in range(len(names)):
    names[i] = names[i].lower()

# prompting user for the letter they'd like to use as starting letter
letter = input("Which letter would you like to use as starting letter?: ").lower()

# output: printing the names that start with the letter they inputted
print(f"the names that start with {letter} are:")
for i in names:
    if i.startswith(letter):
        print(i, end=" ")
print()

# wrapping up the program
print("Thank you for using this program!")
