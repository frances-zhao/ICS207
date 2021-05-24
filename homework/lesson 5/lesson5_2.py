#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 30 2021
#Program Name: Lesson 5_2
#Description: asking the user for temperature
#if over 25, output it is hot, if below 5, output it is cold
#other temperatures = comfortable
#
#*****************************************************

#input: prompting the user for the temperature
temperature = float(input("Please enter the temperature: "))

#process: using if statement to output the smaller integer
if temperature > 25:
	print("It is hot.")
elif 5 > temperature:
	print("It is cold.")
elif 25 <= temperature >= 5:
	print("It is comfortable.")

