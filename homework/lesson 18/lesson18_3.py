# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_3.py
# Description: Write a function which reverses the order of the letters in a word.
# Write your own function to do this, do not use a python function.
# Write a main program which calls your function.
# Call the function with a word inputted by the programmer and another one entered by the user.
#
# *****************************************************

# function to reverse the letters in a word
def reverse_loop(word):
    reversed_word = str()
    length = len(word) - 1  # subtract one to find the indexes of the word
    while length >= 0:
        reversed_word += word[length]  # printing the last letter
        length = length - 1  # subtracting the length so next time, print the second last word
    return reversed_word


# input: prompting the user for the word they want to reverse
word = input("Please input a word you want to reverse: ")
# output: using the function to print the reversed word
print(reverse_loop(word))
