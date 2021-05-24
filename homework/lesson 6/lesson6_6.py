#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 5 2021
#Program Name: Lesson 6_6
#Description:Gather an age in months, then provide the age in whole years
#rounded up or down as appropriate
#
#*****************************************************

#input: prompting the user for their age in months
age = int(input("What is your age in months?: "))

#outputting their age in years rounded to the nearest year.
print(f"Your age in years rounded to the nearest year is: {round(age/12)} years old.")