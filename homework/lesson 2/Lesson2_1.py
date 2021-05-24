#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 26th 2021
#Program Name: Lesson 2_1
#Description: prompting the user for the height and base length of a right angle triangle
#Outputting the area of the triangle
#
#*****************************************************

#variable declaration
height = float()
base = float()

#prompting the user for the height and base of the triangle
height = float(input("Welcome to the right triangle area finder! Please enter the height of the triangle: "))
base = float(input("Please enter the base length of the triangle: "))

#conversion rule to find area of triangle
area = base * height / 2

#outputting the area of the right angle triangle
print("The area of your triangle is ", area, " units squared." )