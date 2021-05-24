#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 27 2021
#Program Name: Lesson3_Distance
#Description: asking the user for coordinates of two points, and computing the distance
#
#*****************************************************
import math

print("Enter the coordinates of the first point: ")
x1=int(input())
y1=int(input())

print("Enter the coordinates of the second point: ")
x2=int(input())
y2=int(input())

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance: 0.2f}.")
