#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_7
#Description: Ask the user for a target number
#display all integers from 1 to the target.
#
#*****************************************************

#variable declaration
num = 1
target = int()

#input: prompting the user for a target number
target = int(input("Please enter a target number: "))

#outputting the numbers from one to the target number
while True:
	if num <= target:
		print(num)
		num +=1
