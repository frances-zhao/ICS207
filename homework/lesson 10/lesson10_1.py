#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 12 2021
#Program Name: Lesson10_1
#Description:Prompt the user for two integers x and n
#use a loop to calculate 1 + x + x^2 + x^3 +... + x^n
#
#*****************************************************

#variable declaration
x = int()
n = int()
sum = int(0)

#input: prompting the user for x and n, the two integers
x = int(input("Please enter an integer (your base): "))
n = int(input("Please enter another integer (your target power): "))

#process: using the for loop, calculate the sum of the powers until the target integer
for i in range(0, n+1):
	sum += x** i

#output: printing the sum of the powers once the loop is complete
print(f"The sum of {n} power withs the base of {x} is {sum}.")