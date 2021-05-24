# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 22 2021
# Program Name: lesson21_2.py
# Description: Write a subprogram that prints a slant. This subprogram should have one parameter where
# you specify the number of rows in the slant.
#
# *****************************************************
# procedure to print out a slant by the number of rows entered
def slant(num):
    x = ""
    for i in range(num):
        x += " "
        print(x + "*")


# variable declaration
n = 4

# testing the procedure
slant(n)
