#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 5 2021
#Program Name: Lesson 6_7
#Description: gather two numbers and ask user for an operation
#output the result of the operation with the two numbers given
#
#*****************************************************

#input: prompting the user for two numbers and an operation
num1 = float(input("Please input your first number: "))
num2 = float(input("Please input your second number: "))
operation = input("Please choose an operation: '+', '-', '*', or '/'.: ")

#process: outputting the result and operation based on the symbol chosen.
if operation == "+":
	print(f"The sum of your two numbers is: {num1 + num2}.")
elif operation == "-":
	print(f"The difference of your two numbers is: {num1-num2}.")
elif operation == "*":
	print(f"The product of your two numbers is: {num1*num2}.")
elif operation == "/":
	if num2 != 0:
		print(f"The quotient of your two numbers is: {num1/num2}.")
	else:
		print("This is an error because you cannot divide any number by zero.")
else: 
	print("You entered an invalid operation symbol.")