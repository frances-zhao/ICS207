#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 8 2021
#Program Name: Lesson5_country
#Description: Ask the user for what country they were born in
#If they were born in Canada do nothing
#If they were born outside Canada ask them how long they have lived in Canada.
#
#*****************************************************

#input: prompting the user for the country they were born in.
country = str(input("What country were you born in?: "))

#outputting and prompting results based on the input from user
if country.lower() == "canada":
	print("I see, thank you.")
else:
	time = input("How many years have you lived in Canada?: ")
	print("That's amazing!")