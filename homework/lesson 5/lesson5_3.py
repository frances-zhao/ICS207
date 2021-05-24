#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 30 2021
#Program Name: Lesson 5_3
#Description: asking the user for positive integer value
#if entered 0 or negative value, print "You did not enter a positive number"
#if even integer: print it's even, if odd: print it's odd.
#
#*****************************************************

#input: prompting the user for a positive integer value
positive_int = int(input("Please enter a positive integer: "))

#process: fulfilling the program by using if, elif, and else statements
if positive_int <=0:
	print("You did not enter a positive number.")
elif positive_int % 2 == 0:
	print("Your integer is even.")
else:
	print("Your integer is odd.")