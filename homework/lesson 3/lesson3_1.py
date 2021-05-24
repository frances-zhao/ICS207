#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 27 2021
#Program Name: Lesson 3_1
#Description: asking the user for the area of a square
#output the side length of the square and its perimeter
#
#*****************************************************

#variable declaration
area = float()

#input: prompting the user for the area of their square
area = float(input("What is the area of your square? "))

#process: conversion rule for the length and perimeter from the area
length = area ** 0.5
perimeter = length * 4

#output: the length and perimeter of the square
print("The length of your square is %0.2f units." % length)
print("The perimeter of your square is %0.2f units." % perimeter)
