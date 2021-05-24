# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_2.py
# Description: Write a function that takes a positive integer as its input (parameter) and
# returns the factorial of that number. Write a program that prompts the user
# for a number and then outputs its factorial. It should do this repetitively until
# the user enters a sentinel value (as chosen by the programmer).
#
# *****************************************************
import math

# variable declaration
num = int(1)


# creating a function that outputs the factorial of a number
def fact(num):
    fact_num = math.factorial(num)
    return fact_num


# process:
while num != 0:  # prompting the user for a number they want
    num = int(input("Please input a number you want to find its factorial (enter 0 to exit): "))
    if num != 0:
        print(math.factorial(num))
    elif num == 0:  # if sentinel value (0) is entered, end program
        print("End of program!")
        break


