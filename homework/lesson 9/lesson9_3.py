#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 11 2021
#Program Name: Lesson9_3
#Description: Write a program that lets the user enter two ints, A and B.
#If A < B count up from A to B. If A > B count down from A to B.
#Extension: Let the user enter a third input, C, which indicates how
#much the counter should increment by
#
#*****************************************************

#variable declaration 
a = int()
b = int()

#input: prompting the user for two integers
a = int(input("Please enter a (first integer): ")) 
b = int(input("Please enter b (second integer): "))

#process + output:
#checking which integer is larger and outputting the counts based on the check
#if a < b, count from a and if a > b, count down from a
if a < b:
    for i in range (a, (b+1)):
        print(i, end = " ")
else: 
    for i in range (a, (b-1), -1):
        print(i, end = " ")

#separation for the extension
print()
print("<< Extension below! >>")
print()

#input: prompting the user for two integer values and a step value
a = int(input("Please enter a (first integer): ")) # starting value
b = int(input("Please enter b (second integer): ")) # ending value
c = int(input("Please enter c step value/ count by...): "))   # step value


#process + output:
#checking which integer is larger and outputting the counts based on the check
#if a < b, count from a and if a > b, count down from a
if a < b:
    for i in range (a, (b+1), c):
        print(i, end = " ")
else: 
    for i in range (a, (b-1), -c):
        print(i, end = " ")
        
