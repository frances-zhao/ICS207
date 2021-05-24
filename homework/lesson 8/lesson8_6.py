#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 11 2021
#Program Name: Lesson8_6
#Description: Write a program to check if one number is factor of another.
#If the user does not enter a positive integer prompt them again (and again and…) until they do. 
#For the second number you should also ensure the value they enter is not more than the
#first number.
#
#*****************************************************
#variable declaration
num_1 = int(-1)
num_2 = int(-1)

#input: prompting the user for the first number
while num_1 <= 0:
    num_1 = int(input("Please enter a positive integer: "))
#input: prompting the user for a second number that is less than the first
while num_2 <= 0 or num_1 <num_2:
    num_2 = int(input("Please enter another positive integer that is less than the first integer: "))
   
#process + output: checking to see if one is the factor of another an outputting result
if num_1 % num_2 == 0:
    print(f"{num_2} is a factor of {num_1}.")
else:
    print(f"{num_2} is not a factor of {num_1}.")
    