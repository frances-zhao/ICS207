#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 10 2021
#Program Name: Lesson8_3
#Description: Ask the user for a positive integer.
#Print the ten times table for that number all on one line.
#
#*****************************************************

#variable declaration
num  = int(0)
step = int(1)

#input: prompting the user for a positive integer
while num <= 0:
    num = int(input("Please enter a positive integer: "))
    
#process: outputting the timestable to ten based on the step/counter
while step <= 10:
    print(f"{step*num}", end = " ")
    step += 1

    