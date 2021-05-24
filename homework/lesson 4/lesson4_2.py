#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 29 2021
#Program Name: Lesson 4_2
#Description: asking the user for their last name 
#outputting the group they are in (2 groups: A-H, I-Z)
#
#*****************************************************

#loop for four students
for i in range(4):

	#input: prompting the user for their last name
	last_name = str(input("What is your last name? "))

	#output: based on their last name, the output will put them in group one or two.
	if "a" <= last_name < "i" or last_name >= "A" <= last_name < "i":
		print("You are in group one.")
	else:
		print("You are in group two.")
	print("Please go to your group.")
	print()
    
