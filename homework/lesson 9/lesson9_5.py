#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 11 2021
#Program Name: Lesson9_5
#Description: Find the sum of first ten cubes.
#
#*****************************************************
x = int()

#printing the first ten squares
for i in range(1, 11):
	x += i ** 3
print(f"The sum of the first ten cubes is {x}.")