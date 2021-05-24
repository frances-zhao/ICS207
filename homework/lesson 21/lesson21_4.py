# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 22 2021
# Program Name: lesson21_4.py
# Description: Create using loops. Write a procedure to output the pattern. In each case the procedure should have
# one parameter which is the number of rows. Test your procedures with input from programmer and from
# user.
#
# *****************************************************
# part a
print("<<<PART A>>>")


# creating a procedure to print out the pattern in a)
def part_a(num):
    num = int(num)
    x = "**"
    for i in range(num, 0, -1):
        print(x * i)


# testing the procedure
num = input("Please input a positive integer: ")  # gathering a number of rows
while not (num.isdigit()):  # making program robust
    num = input("Please input a positive INTEGER: ")
part_a(num)  # printing the pattern

# part b
print("<<<PART B>>>")


# procedure for the third pattern
def triangle(num):
    num = int(num)
    for i in range(0, num):
        for j in range(0, num-i-1):
            print(end=" ")
        for j in range(0, 2 * i + 1):
            print("$", end="")
        print()


# testing the procedure
num = input("Please input a positive integer: ")  # gathering a number of rows
while not (num.isdigit()):  # making program robust
    num = input("Please input a positive INTEGER: ")
triangle(num)  # printing the pattern

# part c
print("<<<PART C>>>")


# creating a procedure for part c patter n
def number_triangle(num):
    num = int(num)
    for i in range(1, num+1):
        for space in range(1, (num-i + 1)):
            print(" ", end="")
        for symbol in range(1, i+1):
            print(i, end="")
        print()


# testing the procedure
num = input("Please input a positive integer: ")  # gathering a number of rows
while not (num.isdigit()):  # making program robust
    num = input("Please input a positive INTEGER: ")
number_triangle(num)  # printing the pattern

# wrapping up the program
print("Thank you for using this program.")
