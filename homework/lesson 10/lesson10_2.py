#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 12 2021
#Program Name: Lesson10_2
#Description: Ask user for temperature, keep doing so until entered a temperature above 30
#when above 30, print "Wow, that's hot.".
#
#*****************************************************

#variable declaration:
temperature = float()

#input: prompting the user for a temperature
temperature = float(input("Please input a temperature: "))

#process: if temperature under 30, prompt user for another temperature
while temperature <30:
	temperature = float(input("Please input another temperature: "))
#output: printing a result if the temperature is 30 or above
print("Wow, that's hot.")