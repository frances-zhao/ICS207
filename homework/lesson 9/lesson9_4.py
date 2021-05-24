#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 11 2021
#Program Name: Lesson9_4
#Description: Use a for loop to find the sum of the first 100 natural numbers.
#Extension: Ask the user for a target number and find the sum of that many natural numbers.
#
#*****************************************************

#variable declaration
num = int()

#outputting the sum of the first 100 natural numbers
for i in range(100):
  num += i+1 #rule to find the sum of the numbers
print(f"The sum of the first 100 natural numbers is {num}.")

print()
print("<<Extension below!>>")
print()

#extension
#resetting the variable to 0
num = int(0)

#input: prompting the user for a target number
target = int(input("Please enter a target number (natural number): "))
for i in range(target):
  num += i+1 #rule to find the sum of the numbers
print(f"The sum of the natural numbers from 1 to {target} is {num}.")
