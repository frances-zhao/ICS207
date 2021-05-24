# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 18 2021
# Program Name: lesson12_3.py
# Description: Prompt the user for ten words. Return the average length of the words entered by the
# user.
#
# *****************************************************

# variable declaration
word = str()  # word inputted
average = int()  # average for
counter = int(0)

# input: using a while loop, prompt the user for a word
while True:
    word = input("Please enter a word (enter 'EXIT' to exit): ")
    if word != "EXIT":  # if word is not EXIT, continue
        length = len(word)  # using the len() function, count the length of the word
        average += length  # adding the length to the average
        counter += 1
    else:  # break loop if the sentinel value EXIT is entered
        break

# output: printing the average length of the words
print(f"The average length of the words you entered is {average/counter} letters. ")
