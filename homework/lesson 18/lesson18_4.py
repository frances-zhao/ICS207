# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_4.py
# Description: Write a function which takes a length in centimeters and returns the length in meters.
# Write a program to test your function.
#
# *****************************************************
# variable declaration
cm = int()


# function to convert cm to meter
def meters_length(cm):
    meters = cm * .01
    return meters


# input: prompting user for the centimeters
cm = float(input("Please input a length in centimeters you want to convert to meters: "))

# using the function meters_length to convert cm to m
print(f"{meters_length(cm)} m")