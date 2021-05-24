#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 12 2021
#Program Name: Lesson10_6
#Description:Ask the user for two numbers. Output their average. 
#Keep doing this until both the numbers are zero.
#
#*****************************************************

#variable declaration
num1 = int()
num2 = int()

#input: prompting the user for two numbers
while True:
	num1 = int(input("Please enter your first number: "))
	num2 = int(input("Please enter your second number: "))
	#outputting 0 if both numbers are 0
	if num1 == 0 and num2 == 0:
		print("Your average is 0.")
		break
	#outputting the average of the two numbers
	else:
		print(f"The average of your two numbers is {(num1+num2)/2}.")