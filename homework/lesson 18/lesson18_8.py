# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 20 2021
# Program Name: lesson18_8.py
# Description: Write a function which removes all vowels from a string that is passed in its parameter. Write a main
# program which prompts the user to enter 5 strings and removes the vowels from each one.
#
# *****************************************************
# creating a function to remove vowels from a string
def remove_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    return word


# input: prompt user for 5 strings and output result
for i in range(5):
    word = input("Please input a word: ")
    while not (word.isalpha()):  # making program robust: making sure the string is alphabetical
        word = input("Please enter a alphabetic word: ")
    print(remove_vowels(word))  # using the remove_vowels function, print result
print("Thank you for using this program!")
