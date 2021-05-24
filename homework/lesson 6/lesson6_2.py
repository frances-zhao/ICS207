#*****************************************************
#
#Program Author: Frances Zhao
#Completion Date: May 2 2021
#Program Name: Lesson 6_2
#Description: Gather a full name, street address, city, and country.
#if the country is Canada, gather the province and postal code, 
#otherwise gather the U.S. state and zip code.
#output the full address on a single line.
#
#*****************************************************

#variable declaration
full_name = str()
address = str()
city = str()
country= str()

#input: prompting the user for their name, address, city, and country
full_name = input("Input your full name: ")
address = input("Input your street address (number and street): ")
city = input("Input the city you live in: ")
country = input("""Do you live in 
1. Canada
or 
2. United States?
""")

#process: asking for the rest of the address in terms of what the user's country is
#outputting the user's address in a single line
if country == "1":
	province = str(input("Which province/territory do you live in?: "))
	postal_code = str(input("Please insert your postal code: "))
	print(f"""Name: {full_name}
Address: {address}
{city} {province} {postal_code}
Canada """)
elif country == "2": 
	us_state = str(input("Which state do you live in?: "))
	zip_code = str(input("Please insert your zip code: "))
	print(f"""Name: {full_name}
Address: {address}
{city} {us_state} {zip_code}
USA """)
else:
	print("Invalid option. Next time, enter 1 or 2.")

