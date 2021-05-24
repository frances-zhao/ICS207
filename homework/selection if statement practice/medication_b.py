#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 8 2021
#Program Name: Lesson5_medication_b
#Description: Write a program which asks the user what day of the week it is
#Vary this program so you also ask the user how often they take their medicine.
#
#*****************************************************

#input: prompting user for the day of the week and how often they use medication
current_day = input("What day of the week is it (assuming that you took your medication today)?:" )
how_often = int(input("How often in days do you take your medication?: "))

#process: conversion rule for how often to the next time the same day
days_wait = how_often * 7

#outputting the result based on the calculations
print(f"You will take your medication on a {current_day} in {days_wait} days.") 
