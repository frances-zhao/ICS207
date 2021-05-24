# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 17 2021
# Program Name: lesson11_1.py
# Description: Write a program which asks the user five times to enter a word with a random number of letters.
# Variation 1: Confirm that the user entered a word that is the correct length. If not, give them an error message.
# Variation 2: As in variation 1, just make them enter the word over and over until they get one of the correct length.
# *****************************************************
# importing the random generator
import random as r

# variable declaration
length = int()

# input: prompt user for a word with random length characters
for i in range(5):  # do this five times
    length = r.randint(1, 10)
    word = input("Please enter a word with " + str(length) + " characters: ")
    while len(word) != length:  # variation 1
        print(f"Error, you did not enter a word with {length} characters.")
        word = input("Please enter a word with " + str(length) + " characters: ")
