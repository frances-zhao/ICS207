# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson19_3.py
# Description: Write a function that tests if an integer is a multiple of 7.
# Write a program to test your function. Do not use user input.
#
# *****************************************************
# function to see if number inputted is a multiple of seven
def multiple_of_seven(num):
    if num % 7 == 0:
        return "Your number is divisible by seven!"
    else:
        return "Your number is not divisible by seven."


# testing the function to see if it works
num = int(50)
print(multiple_of_seven(num))