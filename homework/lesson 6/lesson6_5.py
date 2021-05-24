#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 4 2021
#Program Name: Lesson 6_5
#Description:Modify the program you did earlier which gathered two integer
#display their sum, difference, product, and quotient to guard against division by zero
#
#*****************************************************print("what are your two numbers?")

#input: prompting the user for two integers
num1 = float(input("Please enter your first integer: "))
num2 = float(input("Please enter your second integer: "))

#Process: outputting the sum, difference, product, and quotient based on the integer

if num2 != 0:
    print(f"The sum is {num1+num2}, the difference is {num1-num2}, the product is {num1*num2}, and the quotient is {num1/num2}.")
else:
    print(f"The sum is {num1+num2}, the difference is {num1-num2}, the product is {num1*num2}, and the quotient is an error because it is divided by 0.")