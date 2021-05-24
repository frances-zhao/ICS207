# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson18_1.py
# Description: Write a function that subtracts five from a real number.
# It takes a real as its parameter and returns a real value.
# Next, write a program that uses this function which prompts the user for a number and outputs the new value
# that is returned by the function. Make sure the output is done in the main program, not the function..
#
# *****************************************************
# variable declaration
num = float()


# function: subtracting five from a real number
def subtract_five(num):
    result = num - 5
    return result


# program: prompting user for a number
num = float(input("Please input a real number: "))
print(subtract_five(num))  # using function to print the result
