#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 6 2021
#Program Name: Lesson 7_9
#Description: Write a program to read in a series of positive integers
#output the range of the integers, that is, the interval from the smallest to the largest.
#
#*****************************************************

#variable declaration
num = int()
smallest = int()
largest = int()
average = float()

#input: prompting user for a number from 0-100 and label it as the largest and smallest number
while True:
    num = int(input("Enter a number from 0 to 100 (inclusive): "))
    if num >= 0 and num <= 100:
        break

smallest = num
largest = num

#process: continuing to ask user for numbers until they enter -1
while True:
    num = int(input("You can enter another number from 0 to 100 (enter -1 to exit): "))
    if num == -1:
        break
    while num < 0 or num > 100:
        num = int(input("You entered an invalid number. Try again: "))
        
#comparing the numbers to see which one is larger and smaller
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num  

#outputting the interval of the largest and smallest number
print(f"The smallest number is {smallest} and the largest number is {largest} and the interval between the two is {largest -smallest}.")