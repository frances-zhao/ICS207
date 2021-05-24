#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 28 2021
#Program Name: Lesson3_Groups
#Description: asking the user for the total students and student amount in each group
#outputting number of groups and extra students
#
#*****************************************************

#variable declaration
total_students = int()
students_per_group = int()
normal_groups = int()
larger_groups = int()

#input: prompting user for the total number of students in the class 
#and how many students per group
total_students = input("How many students are in the class: ")
students_per_group = input("How many students is wanted in each group: " )

#process: if the total students can evenly be divided
if total_students%students_per_group == 0:
    normal_groups = int(total_students / students_per_group)
    print(f"{normal_groups} of {students_per_group}")
   
# if there are extra students remaining
else:
    extra = total_students % students_per_group
    normal_groups = int(total_students / students_per_group)
    larger_groups = extra
    normal_groups -= remainder
    print(f"{normal_groups} of {students_per_group}")
    print(f"{larger_groups} of {students_per_group + 1}")