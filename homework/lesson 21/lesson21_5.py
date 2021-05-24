# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 22 2021
# Program Name: lesson21_5.py
# Description: Create using loops. Write a procedure to output the pattern. In each case the procedure should have
# one parameter which is the number of rows. Test your procedures with input from programmer and from
# user.
#
# *****************************************************
import random


# function to replace a with aa
def make_aa(word):
    new_word = str()
    for i in range(len(word)):
        if "aA".find(word[i]) != -1:
            new_word += word[i]+word[i]
        else:
            new_word += word[i]
    return new_word


# function to replace letter b in a string with "ac"
def replace_b(word):
    new_word = str()
    for i in range(len(word)):
        if "bB".find(word[i]) != -1:
            new_word += "ac"
        else:
            new_word += word[i]
    return new_word


# function to randomly insert the letter c in a string
def random_c(word):
    new_word = str()
    length = len(word)-1
    index = random.randint(0, length)
    for i in range(length+1):
        if i == index:
            new_word += "c"
        new_word +=word[i]
    return new_word


# main program:
functioncall = random.randint(1,10)  # function calls = random
for i in range(functioncall):
    selection = [make_aa, replace_b, random_c]
    choices = random.choice(selection)
    word = input("Please enter a word!: ")  # prompting user for a word
    while not (word.isalpha()):
        word = input("Please enter an alphabetical word: ")
    print(f"your word put in a random function is: {choices(word)}.")  # using a random function and printing result
