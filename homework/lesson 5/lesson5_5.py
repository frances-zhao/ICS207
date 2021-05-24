#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 30 2021
#Program Name: Lesson 5_5
#Description: asking the user for the class size, and number of people per group 
#outputting the correct number of groups with extra members
#
#*****************************************************
#variable declaration
class_size = int()
group_size = int()
extra = int()

#input: prompting the user for the class size and group sizes
class_size = int(input("How many students are in the class?: "))
group_size = int(input("How many people do you want per group?: "))

#process: finding the number of groups and if there are extra students or not 
numberofgroups = class_size // group_size
extra = class_size % group_size

#outputting the final result
if extra == 0:
    print(f"All groups have {class_size / group_size} groups of {group_size}.")
else:
    if extra > numberofgroups:
        print(f"there will be {numberofgroups - extra % numberofgroups} group(s) of {group_size +(extra//numberofgroups)} and {extra % numberofgroups} group(s) of {group_size + (extra // numberofgroups)+1}.")
    else:        
        print(f"there will be {(class_size//group_size)-extra} group(s) of {group_size} and {extra} group(s) of {group_size+1}.")
