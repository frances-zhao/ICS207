# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 18 2021
# Program Name: lesson12_2.py
# Description: Prompt the user for ten words. Return the average length of the words entered by the
# user.
#
# *****************************************************

# variable declaration
word = str()
average = int()

# input: using a for loop, prompt the user for a word (ten times)
for i in range(10):
    word = input("Please enter a word: ")
    length = len(word)  # using the len() function, count the length of the word
    average += length  # adding the length to the average

# output: printing the average length of the words
print(f"The average length of the words you entered is {average/10} letters. ")
