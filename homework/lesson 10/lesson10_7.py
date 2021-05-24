#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 12 2021
#Program Name: Lesson10_7
#Description:a) a) Display the cubes of the first 8 numbers.
#b) Try it again but this time display only the sum of those first 8 cubed numbers.
#c) Write the program again but allow the user to specify the largest number
#whose cube you should display. (A program like in part a.)
#d) Try it again but allow the user to specify both the highest and lowest number
#whose cube you should display. (A program like in part a.)
#
#*****************************************************

#part a): Display the cubes of the first 8 numbers.
print("<<PART A>>")
#process + output: calculating the first 8 cubes and printing it out
print("The first 8 cubes of the first 8 natural numbers are:", end = " ")
for i in range(9):
    print(f"{i}**3={i ** 3}", end = "  ")
print()

#part b): Try it again but this time display only the sum of those first 8 cubed numbers.
#variable declaration
sum = int()
#process: calculating the sum of the first 8 cubes
print("<<PART B>>")
for i in range(9):
    sum += i **3
#output: printing the sum of the first 8 cubes
print(f"THe sum of the first 8 cubes of the first 8 natura numbers is: {sum}.")
print()

#part c): Write the program again but allow the user to specify the largest number whose cube you should display. 
print("<<PART C>>")
#variable declaration
num = int()
#input: prompting the user for an integer
num = int(input("Please enter an integer: "))

#process + output: calculating and displaying the first 8 cubes
print(f"The first {num} cubes are: ")
for i in range(1, num + 1):
    print(f"{i}**3={i ** 3} ")
print()

# d) Try it again but allow the user to specify both the highest and lowest number whose cube you should display.
print("<<PART D>>")
# variable declaration
start_value = int()
end_value = int()

#input: prompting the user for their start and ending value
start_value = int(input("Pleae enter your starting value: "))
end_value = int(input("Please enter your ending value: "))
#since the start value cannot be larger than the end value, if that happens, inform the user and ask again
while True:  
	if start_value < end_value:
		break
	else:
		print("The starting value cannot be larger than the ending value.")
		start_value = int(input("Pleae enter your starting value: "))
		end_value = int(input("Please enter your ending value: "))
		
#process + output: printing the cubes of the numbers from the start value to the end value
print(f"The cubes of numbers from {start_value} to {end_value} are: ")
for i in range(start_value, end_value + 1):
    print(f"{i}**3={i**3} ")
print()

print("Thank you for using this program.")
   

