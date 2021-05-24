# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 17 2021
# Program Name: lesson11_3.py
# Description: Write a program that “rolls a die” 20 times (outputting the roll each time)
# a) Outputs how many times it rolls each number (from 1 to 6). HINTS: Use an accumulator(s)
# b) Outputs what was the most common roll?
#
# *****************************************************

import random

# variable declaration
roll = int()

# Process: rolling the dice 20 times randomly and outputting the rolls
for i in range(20):
    roll = random.randint(1, 6)
    print(roll, end=" ")
print()
print("<<<PART A>>>")

# variable declaration
roll = int()
counts = [0] * 6
max_count = 3
max_index = 0

# process: rolling the dice 20 times randomly and outputting the rolls
for i in range(20):
    roll = random.randint(1, 6)  # generating
    print(roll, end=" ")  # printing
    for i in range(6):  # counting the number of times each number has been rolled
        if roll == i + 1:
            counts[i] += 1
print()
# output: printing the number of times a number was rolled
for i in range(6):
    print(f"{i + 1} has been rolled {counts[i]} time(s).")

print("<<<PART B>>>")
# process: going through each random number and checking the number of times each was rolled
max_count = counts[0]
for i in range(1, 6):
    if counts[i] > max_count:
        max_count = counts[i]

# Output: printing the numbers with the maximum number of counts
for i in range(6):
    if counts[i] == max_count:
        print(f"{i + 1} was the most common roll.")
