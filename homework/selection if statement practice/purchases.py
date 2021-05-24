#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 8 2021
#Program Name: Lesson5_purchases
#Description: Toy trucks cost $8.99 and toy ninjas cost $3.99.  
#Ask the user how many of each they would like to purchase and tell them what the total is.  
#Add tax (13%) to the final bill.

#b) Ask the user how much they have to spend and whether they want to buy trucks or ninjas.  
#Compute how many trucks or ninjas they can buy. Try it first without tax, and then account for tax.  
#Let the user know the total bill and how much change they will get.

#c) Ask the user their total budget.
#Buy the same number of ninjas and trucks including tax.  
#If there is enough change for an extra ninja or truck, let the user know. 

#*****************************************************
#variable declaration
truck = 8.99
ninja = 3.99
total = float()
num_trucks = int()
num_ninjas = int()
total = float()
after_tax = float()
change = float()

#input: prompting the user for the number of toy trucks and ninjas they want to buy
num_trucks = int(input("How many toy trucks would you like to buy?: "))
num_ninjas = int(input("How many toy ninjas would you like to buy?: "))

#process: rule to find the total cost including tax
total = (truck * num_trucks + ninja * num_ninjas) * 1.13

#outputting the result based on the inputs and calculations
print(f"The total cost for {num_trucks} trucks and {num_ninjas} ninjas is ${total: 0.2f}.")

#part b

#input: prompting the user for their budget
budget = float(input("How much money do you have?: "))
while True: 
	prefer = input("What do you prefer: trucks or ninjas?: ")
#process: based on the user's preference and budget, calculate how many of the toy the user can buy
	if prefer.lower() == "truck" or prefer.lower() == "trucks":
		num_trucks = int(budget // (truck * 1.13))
		change = budget % (truck * 1.13)
		total = num_trucks * truck 
		after_tax = total * 1.13
#output: the results displayed
		print(f"You can buy {num_trucks} of {prefer} with: ")
		print(f"Cost before tax: ${total:0.2f}")
		print(f"Final bill after tax: {after_tax:0.2f}")
		print(f"Your change is: ${change:.2f}.")
		break
	elif prefer.lower() == "ninja" or prefer.lower() =="ninjas": 
		num_ninjas = int(budget // (ninja * 1.13))
		change = budget % (ninja * 1.13)
		total = num_ninjas * ninja
		after_tax = total * 1.13 
#output: the results displayed
		print(f"You can buy {num_ninjas} of {prefer} with: ")
		print(f"Cost before tax: ${total:0.2f}")
		print(f"Final bill after tax: {after_tax:0.2f}")
		print(f"Your change is: ${change:.2f}.")
		break
	else:
		print("That is not a valid toy.")
		
#part c

#variable declaration
combined_total = (truck + ninja) * 1.13
toys_set = int()
remainder = float()

#input: prompt the user for their budget
budget = float(input("How much money do you have?: "))

#process: based on the budget, calculate how many sets of toys the user can buy
toys_set = int(budget // combined_total)
remainder = budget - toys_set * combined_total

#process: based on the remainder, if there is enough for a truck or ninja, calculate the total with change
if remainder > truck:
    change = budget - (toys_set + 1) * truck * 1.13 -  toys_set * ninja * 1.13
    print(f"With a budget of ${budget:.2f}, you can buy {toys_set + 1} trucks, {toys_set} ninjas and you will have ${change:.2f} of change.")
elif remainder > ninja:
    change = budget - (toys_set + 1) * ninja * 1.13 -  toys_set * truck * 1.13
    print(f"With a budget of  ${budget:.2f}, you can buy {toys_set} trucks, {toys_set + 1} ninjas and you will have ${change:.2f} of change.")
else:  
    print(f"With a budget of ${budget:.2f}, you can buy {toys_set} trucks, {toys_set} ninjas and you will have ${remainder:.2f} of change")    
    