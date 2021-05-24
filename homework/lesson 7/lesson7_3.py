#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_3
#Description: Write a program which prints all odd numbers between 1 and 10.
#
#*****************************************************

#variable declaration
num = int()

#outputting the numbers between 1 and 10 (not including 1) that are odd
while True:
	if (num % 2 == 1) and (1<num<10):
		print(num)
	num+=1
	