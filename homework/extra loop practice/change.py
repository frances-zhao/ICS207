# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 17 2021
# Program Name: change.py
# Description: Prompt and make sure the user enters an amount of cash less than one dollar. Write a program that
# makes change for that. It should output the original amount of money together with a set of coins
# (quarters, dimes, and nickels)that could make up that amount.
# As pennies exit circulation, cash will need to be rounded, either up or down, to the nearest five-cent
# increment.
#
# *****************************************************
amount = float()
quarters = int()
dimes = int()
nickels = int()
quarter_spell = str("quarters")
dime_spell = str("dimes")
nickel_spell = str("nickels")
original = float()

# input: prompt the user for the amount less than a dollar
while True:
    amount = input("Please enter an amount of cash less than $1: ")
    amount = float(amount)
    round(amount, 2)
    if amount > 0 and amount < 1:
        break
    else:
        print("That is not valid. Please try again.")

# process:calculating the amount of each coin needed as well as the spelling required
original = amount
quarters = int(amount//0.25)
amount -= quarters*0.25
dimes = int(amount//0.1)
amount -= dimes*0.1
nickels = int(amount//0.05)
amount -= nickels*0.05

if amount >= 0.03:
    nickels += 1
if quarters == 1:
    quarter_spell = "quarter"
elif dimes == 1:
    dime_spell = "dime"
elif nickels == 1:
    nickel_spell = "nickel"

# output: based on the calculations, output the number of dimes, quarters, and nickels, needed
if quarters > 0 and dimes > 0 and nickels > 0:
    print(f"You are able to have  ${original} with {quarters} {quarter_spell}, {dimes} {dime_spell}, and {nickels} {nickel_spell}.")
elif quarters > 0 and dimes > 0 and nickels == 0:
    print(f"You can able to have ${original} with {quarters} {quarter_spell} and {dimes} {dime_spell}.")
elif quarters > 0 and dimes == 0 and nickels == 0:
    print(f"You can able to have ${original} with {quarters} {quarter_spell}.")
elif quarters == 0 and dimes > 0 and nickels > 0:
    print(f"You can able to have ${original} with {dimes} {dime_spell}, and {nickels} {nickel_spell}.")
elif quarters == 0 and dimes > 0 and nickels == 0:
    print(f"You can able to have ${original} with {dimes} {dime_spell}.")
elif quarters == 0 and dimes == 0 and nickels > 0:
    print(f"You can able to have ${original} with {nickels} {nickel_spell}.")