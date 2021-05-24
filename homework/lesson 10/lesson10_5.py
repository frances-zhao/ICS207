#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 12 2021
#Program Name: Lesson10_5
#Description:Write a program that takes a whole number as input from the user 
#outputs all the factors of that number.
#(Hint: to check whether a number is a factor use mod to check whether the remainder equals zero.
#check every number from 1 up to the user input to see if it is a factor.)
#
#*****************************************************

#variable declaration
num = int()

#input: prompting the user for a whole number
num = int(input("Enter an integer: "))

#process + output: finding and printing all the factors of the integer inputted
print(f"The factor(s) of your number {num} is/are: ")
for i in range (1, num+1):
    if num%i==0:
        print(i)
