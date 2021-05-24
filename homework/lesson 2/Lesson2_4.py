#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 26th 2021
#Program Name: Lesson 2_4
#Description: prompting the user for a two-digit number (10-99) and outputting the last digit
#
#*****************************************************

#variable declaration
num = int()

#input 
num = int(input("Please enter a number between 10 and 99: "))

#finding the last digit
lastdigit = num % 10

#output
print("The last digit of your number is ", lastdigit,".")