# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson16b_2.py
# Description: Write a program which takes a list of strings and counts how many:
# Have length greater than 4
# Have the same starting and ending letter.
#
# *****************************************************
# variable declaration
string = []
amount = int()
counter = int(0)
start_end = []

# input: prompting user for number of strings they want to input and the strings
amount = int(input("How many strings do you want to input?: "))
for i in range(amount):
    string.append(input("Please enter a string: "))

# changing all the characters to lowercase
for i in range(len(string)):
    string[i] = string[i].lower()

# process: finding the strings that have a length more than 4
for i in range(len(string)):
    if len(string[i]) > 4:
        counter += 1

# output: printing the results
print(f"{counter} of the {amount} words you inputted have a length longer than 4.")

# process: finding the strings with the same starting and ending letter
for i in range(0, len(string)):
    if string[i][:1] == string[i][-1:]:
        start_end.append(string[i])

# output: printing the results
print(f"From the words inputted, the words with the same starting and ending letter is: {start_end}.")

# wrapping up the program
print("Thank you for using this program!")