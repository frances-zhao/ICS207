# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson16b_4.py
# Description: Use arrays to gather and store 10 items and the number of that item they have in their inventory.
# Then allow the user to enter an item and let them know how many of that item they have in inventory.
#
# *****************************************************
# variable declaration:
items_list = []
items = str()
num_list = []
numbers = str()

# process
for i in range(10):
    items = input("Please input an item: ")  # input: prompting user for an item
    while not(items.isalpha()):  # making sure the item entered is valid
        items = input("Invalid input! Please enter a word: ")
    items_list.append(items)
    numbers = input("How many of this item do you have?: ")  # input: prompting the user for the numbers of the item
    while not(numbers.isdigit()):  # making sure the number is a digit
        numbers = input("Invalid input! Please enter a number: ")
    num_list.append(numbers)

# process continued: printing out the number of each item inputted
for i in range(len(items_list)):
    print((items_list[i]), ": ", (num_list[i]))

# process continued: prompting the user for the item they want to check
choice = input("Which item would you like to check?: ")
while not(choice.isalpha()):  # making sure that the item entered is a word
    choice = input("Invalid input! Please enter an item you would like to check: ")
num_result = int()

# process: based on the choice, find the number from the num_list that correlates with the item
for i in range(len(items_list)):
    if choice == items_list[i]:
        num_result = num_list[i]

# output: printing the result
print(f"You have {num_result} {choice} in your inventory.")

