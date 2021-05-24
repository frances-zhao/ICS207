#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 12 2021
#Program Name: Lesson10_3
#Description: prompt user for two even numbers
#output all the even numbers between the two numbers
#
#*****************************************************

#variable declaration
num1 = int(1)

#input: prompting the user for an even number until one is inputted
while num1%2==1:
	num1 = int(input("Please enter an even number: "))
	
#variable declaration p.2
num2 = int(1)

#input: prompting the user for another even number
while num2%2==1:
	num2 = int(input("Please enter a second even number: "))
	
#checking which number inputted is greater and counting the even numbers by that
if num1 > num2:
	for i in range(num2, num1+1):
		if i%2 ==0: #check if the current number (i) is even or not
			print(i)
			i +=1
		else:
			i+=1
			
elif num2 > num1:
	for i in range(num1, num2+1):
		if i%2 ==0: #check if the current number (i) is even or not
			print(i)
			i+=1
		else:
			i+=1
			

