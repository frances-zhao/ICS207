# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_5.py
# Description: Write a function which calculates the area of a triangle. It should have two parameters, the height
# and base of the triangle and return the area of the triangle. Write a program to test your function which
# does not get input from the user.
#
# *****************************************************
# variable declaration
height = int(6)
base = int(5)


# function to find the area of triangle
def area_of_triangle(height, base):
    area = height * base / 2
    return area


# pring the statements and results
print(f"height: {height} units")
print(f"base: {base} units")
print(f"area of triangle: {area_of_triangle(height, base)} units squared")
