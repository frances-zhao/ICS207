#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_5
#Description: Ask the user to enter numbers one at a time
#for each number, x, display –x, and reversed
#
#*****************************************************

#prompting the user for a number
x = float(input("Please enter a number: "))

#outputting the result 
while x != 0:
	x *= -1
	print(x)
	x = float(input("Please enter another number: "))
print("0 cannot be negative or positive.")
	
	