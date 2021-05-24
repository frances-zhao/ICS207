#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_1
#Description: asks user a simple arithmetic question, if right congratulate them
#if wrong, tell them it's wrong and ask them again until it's right
#
#*****************************************************

#asking user to enter answer of the arithmetic question
while True: 
	answer = int(input("What is the answer to this simple arithmetic question: 2 * (2+3) - 4?: "))

#determining if the answer is correct or not
	if answer == 6:
		print("Congratulations! 6 is the correct answer.")
		break
	else:
		print(f"{answer} is the wrong answer. Please try again.")

