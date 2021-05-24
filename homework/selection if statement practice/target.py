#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 8 2021
#Program Name: Lesson5_target
#Description: Write a program which asks a user for a target score
#ask the user for five scores
#output how many of the scores are above the target.
#
#*****************************************************

#variable declaration
target = float()
score = float()
counter = int()
above = int()
same = int()

#input: prompting the user for their target score 
target = float(input("What is your target score?: "))

#continue: ask user for their scores
score = float(input("Please enter your first score: "))
counter =1
while counter <5:
    if score > target:
    	counter +=1
    	above +=1
    	score = float(input("Please enter another score: "))
    elif target > score: 
    	counter +=1 
    	score = float(input("Please enter another score: "))
    	if target == score:
    		same +=1
    		counter +=1
    		score = float(input("Please enter another score: "))
    else:
    	same += 1
    	counter += 1
    	score = float(input("Please enter another score: "))

#printing out the results based on the prompts
if same == 0:
	print(f"{above} mark(s) = above your target score.")
else: 
    print(f"{above} mark(s) = above your target score and {same} mark(s) = the same as your target score.")
    