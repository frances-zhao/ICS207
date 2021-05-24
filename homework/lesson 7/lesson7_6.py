#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_6
#Description: Gather a set of non-zero integers
#display the count, sum, and mean of both the positive and the negative values.
#
#*****************************************************

#variable declaration
num = int()
sum = int(0)
counter = int(0)
mean = float()

#input: prompting the user for a non-zero integer
while True:
	num = int(input("Enter any non-zero integer: "))
	if num != 0:
		sum += num
		counter +=1
		break
	else:
		print("You cannot enter a 0.")

#continuing to ask for non zero integers until the user enters 0
while True:
	num = int(input("Continue to input any non-zero integer (enter 0 to exit): "))
	if num == 0:
		break
	else:
		counter +=1
		sum += num
#calculating the mean and outputting all the results
mean = sum/counter
print(f"You inputted {counter} integers. The sum of your integers is {sum} and the mean of your integers is {mean: .2f}.")