# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson19_1.py
# Description: Write a function which does robust input of any integer, positive or negative.
#
# *****************************************************
# creating a function that does robust input of any integer
def int_input(num):
    while num.isdigit():  # if the integer is positive
        return f"your number {num} is a valid integer!"
    while num.startswith("-") and num[1:].isdigit():  # if the integer is negative
        return f"your number {num} is a valid integer!"
    else:
        return f"{num} is not a valid integer!"


# input: prompting user for an integer
num = input("Please input an integer: ")

# output: printing the result based on the function
print(int_input(num))
