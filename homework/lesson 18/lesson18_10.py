# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 18 2021
# Program Name: lesson18_10.py
# Description: Write a function that takes three names as parameters. Each “person” should roll two dice and
# return the name of the person who got the highest roll. Challenge: make your program handle the case
# two or three people get the same roll, rolling again until a “winner” is selected. In your simple main
# program, ask the user for three names and then tell them who goes first on the basis of who got the
# highest roll in your function.
#
# *****************************************************

# import module
import random


# function created for rolling and finding the sum highest rolls
def highest_roll(name1, name2, name3):
    x = random.randint(1, 6) + random.randint(1, 6)
    y = random.randint(1, 6) + random.randint(1, 6)
    z = random.randint(1, 6) + random.randint(1, 6)

# challenge: making sure that the sum isn't the same, if same, tell user and re-roll
    while x == y or y == z or x == z:
        print(f"At least two people have the same sum. The sums were : {x}, {y}, and {z}.")
        print("We will roll again.")
        x = random.randint(1, 6) + random.randint(1, 6)
        y = random.randint(1, 6) + random.randint(1, 6)
        z = random.randint(1, 6) + random.randint(1, 6)

    # printing the sum of rolls of the three names
    print(f"{name1}'s two rolls sum: {x} ")
    print(f"{name2}'s two rolls sum: {y} ")
    print(f"{name3}'s two rolls sum: {z} ")
    # returning the name of the highest roll sum
    if x > y and x > z:
        return name1
    elif y > x and y > z:
        return name2
    elif z > x and z > y:
        return name3


# input: prompting the users for three names
name1 = input("Please input the first name: ")
name2 = input("Please input the second name: ")
name3 = input("Please enter the third name: ")
# output: printing the name with the highest roll using the highest_roll function
print(f"{highest_roll(name1, name2, name3)} has the highest roll! ")
