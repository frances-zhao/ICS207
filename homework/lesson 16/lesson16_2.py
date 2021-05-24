# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson16_2.py
# Description: Write a dice rolling program that (randomly) rolls a pair of dice 50 times.
# Create an array where you store how many times a sum has been rolled.
# After all 50 rolls ask the user what roll they are interested in and tell them how many times that sum was rolled.
#
# *****************************************************
import random as r

# variable declaration
roll_list = [0] * 13  # starting off all lists with 0
roll_list[0] = -1  # roll_list[0] = -1 because you cannot roll a sum of 0
roll_list[1] = -1  # roll_list[1] = -1 because you cannot roll a sum of 1
roll = int()  # the roll
answer = int()  

# process: finding the roll sums 50 times using a for loop
for i in range(50):
    roll = r.randint(1, 6) + r.randint(1, 6)
    roll_list[roll] += 1

# list of each time the sum was rolled (not part of actual question)
"""
for i in range(13):
    print(f"The roll sum of {i} was rolled {roll_list[i]} times.")
"""

# input: asking the user which sum they are interest in
answer = int(input("Which roll sum are you interested in? (2-12): "))
answer = (answer-2) % 11 + 2

# output: printing the result of the user's interest
print(f"The roll sum of {answer} was rolled {roll_list[answer]} times.")