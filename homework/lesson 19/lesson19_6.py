# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson19_6.py
# Description: Write a function to “glue” two strings together. Write another function which reverses a string.
# Now use those two functions to create a machine (third function) that glues together first two strings,
# reverses the result, and then glues on a third string.
#
# *****************************************************
# first function: glues two strings together
def glue_strings(string1, string2):
    glued = string1+string2
    return glued


# second function: reverses a string
def reverse_string(string):
    return string[::-1]


# third function: glues two strings, reverses it, and glues a third string
def glue_reverse(string1, string2, string3):
    glue = str()
    glue = string1 + string2
    reverse = glue[::-1]
    return reverse + string3

# variable declaration
string = "puppy"
string1 = "happy"
string2 = "kitten"
string3 = "rainbows"

# testing the three functions:
print(glue_strings(string1, string2))
print(reverse_string(string))
print(glue_reverse(string1, string2, string3))