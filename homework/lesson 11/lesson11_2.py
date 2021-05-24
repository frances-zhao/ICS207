# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 17 2021
# Program Name: lesson11_2.py
# Description: Write a program that generates 10 random real numbers between 50 and 60.
#
# *****************************************************
# importing random
import random

# process: outputting random real numbers between 50 and 60 ten times
for i in range(10):
    num = random.uniform(50, 60)
    print(num)


