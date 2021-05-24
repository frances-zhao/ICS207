#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 10 2021
#Program Name: Lesson8_4
#Description: Ask the user for a positive integer.
#Print the ten times table for that number all on one line.
#This time, user is allowed to keep using this program until they do not want to (sentinel value)
#
#*****************************************************

#variable declaration
stopOrNot = str("no")
num  = int(0)
step = int(1)

#a while loop in case the user wants to keep using the program
while stopOrNot.lower() == "no" :
	#input: prompting the user for a positive integer
    while num <= 0:
        num = int(input("Please enter a positive integer: "))
        
	#process: outputting the timestable for ten based on the integer inputted
    while step <= 10:
        print(f"{step*num}", end = " ")
        step += 1
    print()
	#process: asking the user if they want to continue or not
    stopOrNot = input("Would you like to stop this program?: (no/yes) ")
    num = 0
    step = 1
 
#outside the loop: thanking the user for using the program
print("Thank you for using this program!")
