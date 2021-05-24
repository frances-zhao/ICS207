# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_6.py
# Description: Write a function that models linear equations. The function should take three numbers as input m, x and b
# Then it should use the relationship y = mx + b to find the value y and return this result.
# The main program will ask the user for the slope (m), and y-intercept (b) of their line once.
# Then, repetitively, it will ask for a x-value and output the corresponding y-value
# until an appropriate sentinel value is reached.
#
# *****************************************************

# variable declaration
m = 0
x = 0
b = 0


# function for finding the y-value
def linear_equation(m, x, b):
    m = int(m)
    x = int(x)
    b = int(b)
    y = m * x + b
    return y


# input: prompting the user for the slope and y-intercept
m = input("Please input a slope: ")
while not(m.isdigit()):  # making program robust: making sure slope is a digit
    m = input("Please input a slope: ")
b = input("Please input your y-intercept: ")
while not(b.isdigit()):  # making program robust: making sure y-intercept is a digit
    b = input("Please input your y-intercept: ")

# process:
while x != "exit":  # exit = sentinel value
    x = input("Please input your x-value (enter 'exit' to stop): ")  # prompting user for x-value
    if x != "exit":
        while not (x.isdigit()):  # making program robust: making sure x-value is a digit
            x = input("Please input a numerical value: ")
        print(linear_equation(m, x, b))  # output: printing the result using the linear_equation function
    else:
        print("Thank you for using this program!")  # once sentinel value is entered, break loop and wrap program
        break
