# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 15 2021
# Program Name: grade.py
# Description: Ask the user to enter a series of grades and a target grade.
# Count how many of the grades they entered are above the target.
# Output both how many exceeded the target and what percentage of the grades were above the target.
#
# *****************************************************

# variable declaration
target_grade = float()  # the target grade inputted
grade = float()  # the grade inputted
counter = int(0)  # counter to track the number of grades entered
above = int(0)  # counter to track how many grades are above the target

# input: prompting the user for a target grade
target_grade = float(input("Please enter your target grade: "))

# input: prompting the user for their first grade
grade = float(input("Please enter a grade: "))

# based on the first grade: categorize if it is above target grade or not
if grade <= target_grade:
    counter += 1
elif grade > target_grade:
    counter += 1
    above += 1

# process: continue to prompt the user for grades until they enter a sentinel value (-1)
while True:
    grade = float(input("Feel free to enter another grade! (enter -1 to exit): "))
    if grade == -1:
        break
    elif grade <= target_grade:
        counter += 1
    elif grade > target_grade:
        counter += 1
        above += 1

# output: printing the number of grades above target grade AND the percentage of grades entered above the target grade
print(f"{above} grade(s) = above your target grade {target_grade}.")
print(f"From the {counter} grades you entered, {above/counter*100:.2f}% of them were above your target grade.")
