#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_4
#Description: asking the user for 5 integers and outputting the average
#
#*****************************************************
#variable declaration
counter = int(0)
total = int(0)

#prompting the user for an integer
num = int(input("Enter an integer: "))
total += num
counter +=1

#continuing to ask the user for integers until 5 are inputted in total
while True:
	if counter <5:
		num = int(input("Enter another integer: "))
		total += num
		counter += 1
	else:
		break
print(f" the average of all 5 integers is: {total/5}.")
