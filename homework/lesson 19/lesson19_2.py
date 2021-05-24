# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson19_2.py
# Description: Write a function which tests whether a word starts with ‘S’ (lower or uppercase).
# Write a program to test your function.
#
# *****************************************************

# function to determine if a word starts with s or S
def starts_with_s(word):
    if word.startswith("s") or word.startswith("S"):
        return "YES IT DOES"
    else:
        return "NO IT DOESN'T"


# input: prompting th user for a word
word = input("Enter a word: ")

# output: printing if the word starts with s or S using the function
print(f"""Does your word {word} start with a 's' or 'S': 
{starts_with_s(word)}.""")
