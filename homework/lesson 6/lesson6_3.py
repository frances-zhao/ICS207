#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 4 2021
#Program Name: Lesson 6_3
#Description: Gather the principal amount of a loan, and a monthly or annual interest rate
#display the interest owing for one year.
#
#*****************************************************

#input: prompting the user for the loan and its interest rate time
loan = float(input("How much loan do you have?: "))
time = str(input("""Is your loan 
1. monthly
or
2. annually
"""))

#process: conversion rule to find the owing from the percentage
percent = float(input("What is the percentage?: "))
owing = percent / 100+1

#output: the result of the owing based on the time for the interest rate
if time == "monthly" or "Montly":
    print(f"At the end of one year, you owe {owing**12*loan}.")
elif time == "annually" or "Annually":
    print(f"At the end of one year, you owe {owing*loan}.")
else:
    print("You did not enter a valid choice.")