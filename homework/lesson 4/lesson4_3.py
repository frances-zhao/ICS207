#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 29 2021
#Program Name: Lesson 4_3
#Description: asking the user for the occasion and giving them the appropriate greeting 
#
#*****************************************************

#variable declaration
while True: 

#prompting the user for the occasion selection
	ans = int(input("""Which occasion is it?
1.Morning
2.Afternoon
3.Evening
4.Night
"""))
	if 1<= ans <= 4:
		break
	print("Not a valid option.")
	print()
	
if ans== 1: 
	print("Good Morning!") 
elif ans== 2:
	print("Good afternoon!") 
elif ans==3:
	print("Good evening!") 
elif ans==4:
	print("Goodnight!") 


		