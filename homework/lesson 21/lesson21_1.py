# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 22 2021
# Program Name: lesson21_1.py
# Description: Write a procedure that takes a string, word, and an integer, n, as inputs and then outputs the
# word to the screen n times. Write a program to test your procedure. Hint, your main program
# may be very short! Don’t ask the user for input but have you (the programmer) choose the word
# and n values.
#
# *****************************************************
# procedure to output a word n times
def output_word(word, n):
    for i in range(n):
        print(word)


# variable declaration
word = "dog"
n = 9

# testing to see if the procedure works or not
output_word(word, n)
