#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 27 2021
#Program Name: Lesson3_Average
#Description: asking the user for three marks and a course name(#outputting their average)
#
#*****************************************************

#variable declaration
marks = float()
course = str()
total_mark = marks
average = total_mark / 3


#prompting the user for three marks
marks = input("Enter 3 marks: ").split()
mark1, mark2, mark3 = marks
course = input("Enter a course name: ")
mark1 = float(mark1)
mark2 = float(mark2)
mark3 = float(mark3)


#conversion rule for finding the average

average = (mark1 + mark2 + mark3)/3

#outputting the average of the course marks
print(f"Your {course} average is {average}.")
