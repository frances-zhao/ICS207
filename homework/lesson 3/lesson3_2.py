#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 27 2021
#Program Name: Lesson 3_1
#Description: asking the user for the number of students in each IB math class (4 total)
# outputting the total number of gr.9 IB students and the average in each class
#
#*****************************************************

#variable declaration
math_class = int()
total_students = 0.0

#inputting the number of students in each math class
math_class = int(input("How many students are in the first math class? "))
total_students += math_class
math_class = int(input("How many students are in the second math class? "))
total_students += math_class
math_class = int(input("How many students are in the third math class? "))
total_students += math_class
math_class = int(input("How many students are in the fourth math class? "))
total_students += math_class

#process: conversion rule for the average amount of students per class
average = total_students/4

#output: the total number of students in IB (assuming all are enrolled in the math class)
#output: the average amount of students per math class
print(f"There are {total_students} grade nine IB students and around {average} students in each math class.")

