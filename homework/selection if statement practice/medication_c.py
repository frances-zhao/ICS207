#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 8 2021
#Program Name: Lesson5_medication_c
#Description: Write a program which asks the user what day of the week it is
#Vary this program so you also ask the user how often they take their medicine.
#
#*****************************************************

#input: prompting user for the day of the week and how often they use medication
current_day = input("What day of the week is it (assuming that you took your medication today)?:" )
interest_day = input("What day of the week are you interested in including?: ")
how_often = int(input("How often in days do you take your medication?: "))

#process: converting the current_day from a string into an int based on days of the week
if current_day.lower() == "monday":
    current_day = 1
elif current_day.lower() == "tuesday":
    current_day = 2
elif current_day.lower() == "wednesday":
    current_day = 3
elif current_day.lower() == "thursday":
    current_day = 4
elif current_day.lower() == "friday":
    current_day = 5
elif current_day.lower() == "saturday":
    current_day = 6
elif current_day.lower() == "sunday":
    current_day = 7
else:
    print("That is not an available day of the week.")
    
#process: converting the interest_day from a string into an int based on days of the week
if interest_day.lower() == "monday":
    interest_day_num = 1
elif interest_day.lower() == "tuesday":
    interest_day_num = 2
elif interest_day.lower() == "wednesday":
    interest_day_num = 3
elif interest_day.lower() == "thursday":
    interest_day_num = 4
elif interest_day.lower() == "friday":
    interest_day_num = 5
elif interest_day.lower() == "saturday":
    interest_day_num = 6
elif interest_day.lower() == "sunday":
    interest_day_num = 7
else:
    print("That is not an available day of the week.")
    
#process: conversion rule to find the days waiting based on the inputs
if interest_day_num - current_day > 0:
    days_wait = (interest_day_num - current_day) * how_often
else:
    days_wait = (interest_day_num - current_day + 7) * how_often

#outputting the result from the calculations
print(f"You will next take your medicine on a {interest_day} in {days_wait} days.")
