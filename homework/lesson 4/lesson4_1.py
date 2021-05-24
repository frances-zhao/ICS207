#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 29 2021
#Program Name: Lesson 4_1
#Description: asking the user for a real number that = the area of a figure
#assume it's a circle: output the radius and circumference
#assume it's a square: output the length, width, and perimeter.
#
#*****************************************************
import math
#variable declaration
area = float()
radius = float()
circumference = float()
length = float()
perimeter = float()

#input: prompting the user for the area of the figure
area =float(input("What is the area? "))

#process: rule to find the area and circumference of circle
radius = math.sqrt (area / math.pi)
circumference = 2 * math.pi * radius

#output: printing the radius and circumference assuming the area is of a circle
print(f"Assuming the area is of a circle, The radius is{radius: .2f} units.")
print(f"The circumference of the circle is{circumference: 0.2f} units.")

#process: rule to find the length/width and perimeter of a square
length = math.sqrt(area)
perimeter = length * 4

#output: printing the length/width and perimeter assuming the are is of a square
print(f"Assuming the area is of a square, The length and width are both{length: 0.2f} units.")
print(f"The perimeter of the square is{perimeter: 0.2f} units.")
