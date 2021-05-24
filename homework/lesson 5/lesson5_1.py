#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 30 2021
#Program Name: Lesson 5_1
#Description: asking the user two input two ints.
#output which integer is smaller
#
#*****************************************************

#input: prompting the user for two integers
integers = input("Please input two integers: ").split()
int1, int2 = integers
int1 = int(int1)
int2 = int(int2)

#process: using if statement to output the smaller integer
if int1 < int2:
	print(f"The smaller integer is {int1}.")
else:
	print(f"The smaller integer is {int2}.")