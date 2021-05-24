# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 19 2021
# Program Name: lesson16_1.py
# Description: Create an array of ten real numbers. Prompt the user for the daily high
# temperature for the last ten days and store each number in one element of the array.
# Output the temperatures in reverse.
# Calculate (and output) the average temperature. Make sure you do this
# from the data in the array, not as the user enters the data.
# Look through the array for the highest (lowest) temperature. Again,
# search the array, don’t do this as the user enters the data.
#
# *****************************************************


# variable declaration:
list = []
average = float()
highest = float()

# input: prompting the user for ten temperatures
for i in range(10):
    list.append(float(input("Please input the highest temperature of the day: ")))

# process: printing the temperatures in reverse order
print(f"your temperatures in reverse order is:")
for i in range(9, -1, -1):
    print(list[i])

# process: finding the average of the temperatures and printing it
average = sum(list) / len(list)
print(f"The average of your ten temperatures over ten days is {average} degrees.")


# creating a function to find the largest temperature inputted
def highest_temperature(list):
    highest = 0
    for i in range(0, len(list)):
        if (list[i] > highest):
            highest = list[i]
    return highest


# output: printing the highest temperature
print(f"The highest temperature from the ones entered is {highest_temperature(list)} degrees.")


# creating a function to find the lowest temperature inputted
def lowest_temperature(list):
    lowest = list[0]
    for i in range(0, len(list)):
        if (list[i] < lowest):
            lowest = list[i]
    return lowest


# output: printing the lowest temperature
print(f"The lowest temperature from the ones entered is {lowest_temperature(list)} degrees.")