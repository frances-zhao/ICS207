# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 22 2021
# Program Name: lesson21_3.py
# Description: Your program should use the subprogram to produce 7 stars slant if entered a 6
#
# *****************************************************
# procedure to print out a slant by the number of rows entered
def slant(num):
    x = ""
    for i in range(num+1):
        x += " "
        print(x + "*")


# variable declaration
n = 4

# testing the procedure
slant(n)
