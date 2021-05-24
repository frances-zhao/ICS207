# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_7.py
# Description: Write a function that takes a character and if it is a vowel returns “*” and if it is anything else just
# returns the original character. Use your function to change all the vowels in a word entered by the user to *.
#
# *****************************************************
# function to replace vowels with "*"
def replace_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in word:
        if i in vowels:
            new_word = word.replace(i, "*")
    return new_word


# input: prompting the user for a word
word = input("Please input a word: ")
while not(word.isalpha()):  # making program robust: making sure the string is alphabetical
    word = input("Please enter a alphabetic word: ")
print(replace_vowels(word))  # using the replace_vowels function, print result
