# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_9.py
# Description: Write a function which takes two strings and returns the one that is longer in length.
# Write a main program which takes 10 strings from the user and outputs the longest one.
# If there are several strings of the same length, output the first one received of that length.
#
# *****************************************************
# function to find the longest word between two strings
def longest_string(string1, string2):
    if len(string1) > len(string2):
        return string1
    elif len(string2) > len(string1):
        return string2
    else:
        return "The strings are both the same length."


# input: prompting the user for two strings
string1 = input("Please input a string: ")
string2 = input("Please input another string: ")
print(longest_string(string1, string2))  # using longest_string function, print the longer string


# PART TWO
print("<<<PART 2!>>>")

# variable declaration
list = []

# input: prompting the user for ten strings into a list
for i in range(10):
    word = input("Please input a string: ")
    list.append(word)

# process: using a for loop, find the longest string of the list
max_length = -1
for i in list:
    if len(i) > max_length:
        max_length = len(i)
        word = i


# printing result
print(f"The list of words: {list}")
print(f"The string with the longest length is: {word}")

