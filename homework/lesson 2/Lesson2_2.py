#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 26th 2021
#Program Name: Lesson 2_2
#Description: prompting the user for their name, age, and amount in their bank account
#Printing out the information in a specific format
#
#*****************************************************

#variable declaration
name = str()
age = int()
amount = float()

#prompting the user for their name, age, and amount of money in bank account
name = str(input("Hello! What is your name?"))
print("Hello " + name + "! How old are you? ")
age = input()
amount = float(input("How much money is in your bank account? $"))

#outputting the information of the user in a specific format
print("Your name is:", name + ".")
print("You are", age, "years old.")
print("You have $" + str(amount), "in your bank account.")