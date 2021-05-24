#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 4 2021
#Program Name: Lesson 6_4
#Description:Gather the price of an item and its tax status (taxable or nontaxable)
#display a receipt showing the price, PST, GST, and the total
#
#*****************************************************

#input: prompting the user for the price of the item and if the item is taxable or not
price = float(input("What is the price of your item in dollars?: "))
taxable = input("Is your item taxable? yes or no?: ")

#process: PST and GST percentage as well as the rule for the taxes
PST = 0.08
GST = 0.05
pstTax = PST * price
gstTax = GST * price

#output: based on the answer, output the correct results
if taxable == "yes" or "Yes":
	print(f"The price of your item is ${price}.")
	print(f"The PST of your item is ${pstTax: 0.2f}.")
	print(f"The GST of your item is ${gstTax: 0.2f}.")
	print("The total cost of your item is ${price + pstTax + gstTax}.")
else:
	print("The price of your item is ${price}.")