# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson16b_3.py
# Description: Write a program which takes a list of strings and sorts it alphabetically.
# Challenge: Have it sorted alphabetically except all entries that start with “x”
# (upper or lowercase) come first.
#
# *****************************************************

# variable declaration
string_list = []
words = str()

# input: prompting user for words until they enter EXIT
while words != "exit":
    words = input("Enter a word (type 'exit' to stop): ").lower()
    if words != "exit":
        string_list.append(words)

# process: sorting the words by alphabetical order
for i in range(len(string_list)):
    string_list.sort()

# output: printing the result
print(f"your list in alphabetical order is: {string_list}.")

# CHALLENGE
print("<<<CHALLENGE!!>>>")

# variable declaration
string_list = []
words = str()
yes_x = []
no_x = []
x_sorted = []
remainder_sort = []

# input: prompting the user for words until EXIT is entered
while words != "exit":
    words = input("Enter a word (type 'exit' to stop): ").lower()
    if words != "exit":
        string_list.append(words)

# process: sorting the strings in the list
for i in range(len(string_list)):
    if "xX".find(string_list[i][0]) == -1:  # if xX is not found (-1), put it in the no_x list
        no_x.append(string_list[i])
    else:  # else put it in the yes_x list
        yes_x.append(string_list[i])

# process continued: sorting the two lists in alphabetical order
x_sorted = sorted(yes_x)
remainder_sort = sorted(no_x)

# output: printing the final result
print(x_sorted + remainder_sort)
