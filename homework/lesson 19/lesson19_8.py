# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 21 2021
# Program Name: lesson19_8.py
# Description: Write a function which takes a string and a character as input and removes all occurrences of that
# character from with the string. Test your function.
#
# *****************************************************
# function to remove a letter from a string
def remove_letter(string):
    for i in string:
        new_word = string.replace("t", "")
    return new_word


# variable declaration
string = "spaghetti"
# testing the function
print(remove_letter(string))