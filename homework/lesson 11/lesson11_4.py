# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 17 2021
# Program Name: lesson11_3.py
# Description: Write a “guessing game” program. The computer generates a random number between 1 and 100.
# The user has to try and guess the number.
# After each guess the user makes you tell them whether the number is higher or lower than the guess.
#
# *****************************************************

import random

# variable declaration
secretNumber = int()
numberGuessed = int()

# prompting the computer for a random integer between 1 and 100
secretNumber = random.randint(1, 100)

# process:
while numberGuessed != secretNumber:
    numberGuessed = int(input("Please guess my secret number: "))  # prompting user for their guess
    if numberGuessed < secretNumber:
        print("TOO LOW!")  # printing too low if the guess is smaller than the secret number
    elif numberGuessed > secretNumber:
        print("TOO HIGH!")  # printing too high if the guess is larger than the secret number

# output: once the user guesses the number, outside the loop congratulate the,
print(f"You got it! The number is {secretNumber}.")


