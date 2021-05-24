# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 21 2021
# Program Name: lesson19_9.py
# Description:Write a function which takes a string as a parameter and returns the middle character in the string. If
# there are an even number of characters it should return the first of the two middle characters.
#
# *****************************************************
# function that returns the middle character of a string
def middle_character(string):
    length = len(string)
    if length % 2 != 0:  # if string length is odd: find middle
        middle_letter = length // 2
        return string[middle_letter]
    else:  # if string length is even, subtract one from result to find first middle character
        middle_letter = length // 2 - 1
        return string[middle_letter]


# testing to see if function works
string = "rainbows"
print(middle_character(string))

