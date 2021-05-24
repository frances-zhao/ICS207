#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 1 2021
#Program Name: Lesson 6_1
#Description: asking user if they want to convert inch to cm or cm to inch
#gather measurements and output correct conversion
#
#*****************************************************

#variable declaration
choice = str()

#input: prompting user for their choice: converting cm to inch or inch to cm
choice = input("""Would you like to: 
1. convert inches to centimeters
or
2. convert centimeters to inches?
""")

#process and output: based on their choice, prompt for the inches/cm and convert	
if choice == "1":
	inch = float(input("Please enter the inches: "))
	conversion = 2.54 * inch
	print(f"Your number of inches converted into centimeters is: {conversion} cm.")
elif choice == "2":
	cm = float(input("Please enter the centimeters: "))
	conversion = cm / 2.54
	print(f"Your number of centimeters converted into inches is: {conversion} inches.")
else:
	print("Your choice is invalid. Next time, input either 1 or 2.")
	