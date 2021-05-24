#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 29 2021
#Program Name: Lesson 4_4
#Description: program that reads in a taxable income and outputs the federal tax payable to nearest cent
# first $27,500: pay 17%, on the next $27,500 you pay 24%, and on the rest: 29%
#
#*****************************************************

#variable declaration
income = float()

#input: prompting the user for their taxable income
while True:
	income = float(input("Hello, please enter your taxable income: "))
	if income > 0:
		break
	print("This is an invalid income.")

#process: using if statements to determine the user's federal tax payable based on their income
if income <= 27500:
	print(f"Your federal tax payable to the nearest cent is:{0.17 * income //1: 0.0f} dollars and{0.17 * income %1 * 100: 2.0f} cents.")
elif income <= 55000:
	print(f"Your federal tax payable to the nearest cent is:{(27500 * 0.17 + (income - 27500) * 0.24)//1: 0.0f} dollars and{(27500 * 0.17 + (income - 27500) * 0.24) %1 * 100: 2.0f} cents.")
else:
	print(f"Your federal tax payable to the nearest cent is:{(27500 * 0.17 + 27500 * 0.24 + (income - 55000) * 0.29) //1: 0.0f} dollars and{(27500 * 0.17 + 27500 * 0.24 + (income - 55000) * 0.29) %1 * 100: 2.0f} cents.")