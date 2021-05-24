# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 15 2021
# Program Name: guessing.py
# Description: Make a guessing game. Have the programmer pick a number.
# Have the user guess. Each time tell them if their guess is too high or too low.
#
# *****************************************************

# variable declaration
guess = int()
num = 26

# input: prompting the user for their guess of the number
guess = int(input("Welcome to the guessing game! Please guess a number : "))

# process: based on the guess, tell the user if their guess is correct, too high, or too low
while True:
    if guess < num:  # if the guess is too low
        print("Your guess is too low!")
        guess = int(input("Please guess another number!: "))
    elif guess > num:  # if the guess is too high
        print("Your guess is too high!")
        guess = int(input("Please guess another number!: "))
    elif guess == num:  # if the guess is correct and is the same as the number programmer chose
        print("Your guess is correct!!")
        break
