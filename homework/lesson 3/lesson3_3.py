#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: April 27 2021
#Program Name: Lesson 3_3
#Description: asking the user for three types of items,the quantity of each, and the price of each
#outputting the total amount of money spent on the items
#
#*****************************************************

#input: prompting the user for the three types of items bought
item_list = input("Please enter the three types of items you bought: ").split()

print(item_list)
item1, item2, item3 = item_list

#input: prompting the user for the amount of each item bought
quantity = input(f"Enter the amount of {item1}s, {item2}s, and {item3}s you bought for each: ").split()

print(quantity)
quantity1, quantity2, quantity3 = quantity
quantity1 = float(quantity1)
quantity2 = float(quantity2)
quantity3 = float(quantity3)
print(f"You bought{quantity1: 0.0f} {item1}s,{quantity2: 0.0f} {item2}s, and{quantity3: 0.0f} {item3}s.") 

#prompting the user for the price of one of each item
cost = input("List how much one of each item cost in dollars: ").split()

print(cost)
cost1, cost2, cost3 = cost
cost1 = float(cost1)
cost2 = float(cost2)
cost3 = float(cost3)
print (f"One {item1} costs {cost1} dollars, one {item2} costs {cost2} dollars, and one {item3} costs {cost3} dollars.")

#output: total bill of all the items together
total_cost = quantity1 * cost1 + quantity2 * cost2 + quantity3 + cost3
print(f"Your total bill is:{total_cost //1: 0.0f} dollars and{total_cost % 1 * 100: 2.0f} cents.")