#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 28 2021
#Program Name: Lesson3_Cost
#Description: asking the user for the price of a book and outputting total wholesale cost
#with 40% discount, $2.5 shipping for first copy + 55 cents for each additional copy
#asking user for number of books and display of total cost of that number
#*****************************************************

#variable declaration
price = float()
num = float()
num = 60

#input: prompting user for the price of the book
price = float(input("What is the price of the book in dollars: "))

#conversion rule to find the total cost of 60 copies
price_1 = (price * 0.6) * num + 2.5 + (num-1) * 0.55
print(f"The total cost for 60 copies with shipping and 40% discount is:{price_1 //1: 0.0f} dollars and{price_1 % 1 * 100: 2.0f} cents.")

#input: prompting user for the number of copies
num = float(input("How many books would you like to order: "))

#outputting the total cost for the number of copies
price_1 = (price * 0.6) * num + 2.5 + (num-1) * 0.55
print(f"The total cost for {num} copies with shipping and 40% discount is:{price_1 //1: 0.0f} dollars and{price_1 % 1 * 100: 2.0f} cents.")