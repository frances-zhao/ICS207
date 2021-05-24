# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 15 2021
# Program Name: digit.py
# Description: Write a program that takes an integer as inputs
# Outputs the number of times the digit zero occurs in the number.
# Hint: No use of strings allowed. You may use // and % alternately
# Extension: Allow the user to specify not only the number but which digit we are counting…
#
# *****************************************************

# variable declaration
num = int()
counter = int(0)  # counter to keep track of the number of counting digit chosen
last_digit = int()  # last digit of each number after the modulus and floor divisions
original_number = int()  # original number without all the math calculations

# input: prompting the user for their integer
num = int(input("Please enter a positive integer: "))
original_number = num  # keeping track of the original number for final output

# input: in case the inputted integer is negative, ask the user for a positive one
while num < 0:
    num = int(input("Please enter a POSITIVE integer: "))
    original_number = num  # keeping track of the original number for final output

# process: while the number is larger than 0, find the last digit of each number and see if it is a 0 or not
while num > 0:
    last_digit = num % 10
    num = num // 10
    if last_digit == 0:  # checking if the last digit is 0 or not
        counter += 1  # counter to keep track of number of zeros

# output: printing the number of zeros from the original number
print(f"There are {counter} '0's in your number {original_number}.")
print()

# part #2: extension
print("<<<EXTENSION>>>")

# resetting the counter variable
counter = int(0)

# input: prompting the user for a positive integer
num = int(input("Please enter a positive integer: "))
original_number = num

# input: in case the inputted integer is negative, ask the user for a positive one
while num < 0:
    num = int(input("Please enter a POSITIVE integer: "))
    original_number = num  # keeping track of the original number for final output

# input: prompting the user for the digit that they'd like to be counted
chosen_digit = int(input("Please enter the digit you want to get counted: "))

# in case chosen_digit is more than one digit, prompt the user for one digit only
while chosen_digit > 9 or chosen_digit < 0:
    chosen_digit = int(input("Please enter ONE digit you want to get counted: "))

# process: checking if the last digit before each floor division is the chosen_digit or not
while num > 0:
    last_digit = num % 10
    num = num // 10
    if last_digit == chosen_digit:  # checking if the last digit is 0 or not
        counter += 1  # counter to keep track of number of zeros

# output: printing the number of chosen_digit from the original number and wrapping up the program
print(f"There are {counter} '{chosen_digit}'s in your number {original_number}.")
print("Thank you for using this program!")
