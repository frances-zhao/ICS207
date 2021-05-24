# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 15 2021
# Program Name: population.py
# Description: The country A has 50M inhabitants, and its population grows 3% per year.
# The country B, 70M and grows 2% per year. Determine in how many years the population of
# country A will surpass country B.
#
# *****************************************************

# variable declaration
population_a = 50000000  # population for country a
population_b = 70000000  # population for country b
counter = int(0)  # counter for the number of years

# showing the user that current statistics of the two countries
print("Country A has 50 million inhabitants and its population grows 3% every year.")
print("Country B has 70 million inhabitants and its population grows 2% every year.")

# process: using a while loop to calculate how much each population increases overtime
while population_a < population_b:
    population_a *= 1.03
    population_b *= 1.02
    counter += 1

# output: printing the number of years and ending the program
print(f"It will take {counter} years for country A's population to surpass country B.")
