# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson19_5.py
# Description: Write a function that doubles a value. Write a program that asks the user for a number and then
# keeps doubling (and outputting) that number until a maximum (1000, 1000000 perhaps?) of your choice
# is reached.
#
# *****************************************************
# function that doubles the value until a maximum
def doubling(value):
    value = int(value)
    while value < 1000:
        print(value)
        value *= 2
    return "This is the value doubled until a maximum of 1000."


# input: prompting the user for a number
value = input("Please input a number:")
while not (value.isdigit()):  # checking if number is robust
    value = input("Please input a NUMERICAL number: ")

# output: printing the results
print(doubling(value))
