#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 10 2021
#Program Name: Lesson8_2
#Description: Ask the user for the heights in cm of a group of people.
#Allow the user to enter as many heights as they want. 
#Choose an appropriate sentinel value. 
#Find the average of all the heights they entered.
#
#*****************************************************

#variable declaration
height = float()
total_height = float(0)
heights_entered = int(0)

#input: prompting the user for a height (positive number)
while True:
	height = float(input("Please input the height of a person in cm: "))
	total_height += height
	if height <=0:
		print("You cannot have 0 or a negative number as a height. ")
	else:
		break

#process: asking for more heights until user enter 0 (sentinel value to break the loop)
while True:
	if height > 0:
		height = float(input("Please enter another height (enter 0 to exit): "))
		total_height += height
		heights_entered +=1
	elif height ==0: #if entered 0, loop will end and average is outputted
		average = total_height / heights_entered
		print(f"The average of the {heights_entered} height(s) entered is {average} cm.")
		break
	elif height <0: #if negative, loop will end 
		print("You cannot enter a negative height.")
		break