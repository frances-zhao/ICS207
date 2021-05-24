# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson19_4.py
# Description: A word is a palindrome if it is the same in reverse. You should write a function that checks whether a
# specific word is a palindrome. Write a program to test your function.
#
# *****************************************************
# creating a function to reverse the word
def palindrome(word):
    return word[::-1]


# input: prompting the user for a word they want to check
word = input("Please input a word you want to check: ")

# output: printing if the word is a palindrome or not
if palindrome(word) == word:
    print(f"Your word <<{word}>> is a palindrome!")
else:
    print(f"Your word <<{word}>> is NOT a palindrome.")