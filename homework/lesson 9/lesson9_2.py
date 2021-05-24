#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 11 2021
#Program Name: Lesson9_2
#Description: Change the program to instead ask the user for a starting number and ending number. 
#Use a for loop to count from the first number to the second number.
#Extension: Do not assume the user enters a smaller number first.
#Check which input is smaller before counting.
#
#*****************************************************

#variable declaration
num = int()
num1 = int()
num2 = int()

#input: prompting the user for two numbers (starting and ending)
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

#checking which input is larger and outputting the numbers in between based on the check
if num1>num2 : 
	for num in range(num2, (num1+1)):
		print(num)
else:
	for num in range(num1, (num2+1)):
		print(num)