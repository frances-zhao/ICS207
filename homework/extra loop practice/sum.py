# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 14 2021
# Program Name: sum.py
# Description: User enters two positive integers, the first lower than the second.
# The program computes the sum of adding all the numbers from the lower bound to the upper bound
# Make sure you do error checking to confirm the first number is lower than the second.
#
# *****************************************************

# variable declaration:
x = int(-1)  # the first integer
y = int(-1)  # the second integer
total_sum = int(0)  # the total sum of the integers from x to y

# input: prompting the user for a positive integer
while x <= 0:  # making sure the final integer is positive
    x = int(input("Please enter a positive integer: "))

# input: prompting the user for a second positive integer
while y <= 0:  # making sure the second integer is positive
    y = int(input("Please enter a second positive integer: "))
while y <= x:  # checking if the second integer is larger than the first integer
    y = int(input("Please enter a second positive integer HIGHER than the first: "))

# process: using a for loop, calculating the total sum of the integers between x and y
for i in range(x, y + 1):
    total_sum += i
    i += 1

# output: printing the total sum of integers from x to y and ending the program
print(f"The sum of the numbers from {x} to {y} is {total_sum}.")
print("Thank you for using this program!")
