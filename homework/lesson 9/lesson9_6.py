#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 11 2021
#Program Name: Lesson9_6
#Description: Find the factorial of a number n entered by the user.
#
#*****************************************************

#variable declaration
num = int(-1)
factorial = int(1)

#input: prompting the user for a positive integer
while num < 1:
    num = int(input("Please enter a positive integer: "))

#process: finding the factorial for the number inputted
for i in range(num, 0, -1):
    factorial *= i #rule for finding the factorial

#output: printing the factorial
print(f"The factorial of {num} is {factorial}.")