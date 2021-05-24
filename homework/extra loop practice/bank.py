# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 15 2021
# Program Name: bank.py
# Description: Julia has $300 in her bank account earning 1.25% annual interest
# Max has only $280 but he earns 2% annual interest
# Write a program which uses a loop to compute how many years before Max has more money in his account than Julia?
#
# *****************************************************

# variable declaration
max_money = 280
julia_money = 300
counter = int(0)

# showing the user the current amount of money each person has and their annual interests
print("Julia currently has $300 in her bank account and earns a 1.25% annual interest.")
print("Max currently has $280 in his bank account and earns a 2% annual interest.")

# process: formula to finding the money in each person's bank account until max has more money than julia
while max_money < julia_money:
    max_money *= 1.02  # max's money increasing by 2% every year

    julia_money *= 1.0125  # julia's money increasing by 1.25% every year
    counter += 1  # counter to keep track of the years it takes

# output: printing the number of years it will take max to get more money in his account than julia
print(f"It will take Max {counter} years to get more money in his account than Julia.")
