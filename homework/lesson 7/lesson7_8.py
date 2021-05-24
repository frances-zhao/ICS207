#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_8
#Description: Write a program which prompts the user for two positive integers
#finds the LCM of those two numbers
#
#*****************************************************
import math

#variable declaration
num1 = int()
num2= int()
multiple = int()
inc = int()

#input: prompting the user for two positive integers
num1 = int(input("Please enter your first positive integer: "))
while num1 < 0:
	num1= int(input("That is not a positive integer. Please enter a positive integer: "))
num2 = int(input("Please enter your second positive integer: "))
while num2 < 0:
	num2 = int(input("That is not a positive integer. Please enter a positive integer: "))

#determining which integer is the multiple
if num1 > num2:
	multiple = num1
else:
	multiple = num2
	
#process: updating the multiple
inc = multiple
while multiple % num1 != 0 or multiple % num2 != 0:
	multiple += inc

#outputting the LCM based on the two positive integers given
print(f"The LCM of {num1} and {num2} is {multiple}.")