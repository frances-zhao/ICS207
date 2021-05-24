#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 30 2021
#Program Name: Lesson 5_4
#Description: Asking the user for a number, if multiple of 5, print that effect
#if not a multiple of 5, tell them to enter a multiple of 5 next time.
#
#*****************************************************

user_number = int(input("Enter a number: "))

if user_number % 5 == 0:
	print("Your number is a multiple of five.")
else:
	print(f"Your number is {user_number}. Next time, enter a multiple of five.")