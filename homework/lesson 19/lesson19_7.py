# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 21 2021
# Program Name: lesson19_7.py
# Description: Write a function which takes two numbers as input and returns true if the first number is a factor of
# the second, false otherwise. Test your function with programmer input.
#
# *****************************************************
# function to check if a number is a factor of a second number inputted
def factor_result(num1, num2):
    if num2 % num1 == 0:
        return True
    else:
        return False


# variable declaration (programmer input)
num1 = 4
num2 = 12

# testing to see if the function works or not
print(factor_result(num1, num2))