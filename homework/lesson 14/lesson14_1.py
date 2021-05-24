# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 18 2021
# Program Name: lesson14_1.py
# Description: a) Write a program that asks the user to enter words
# calculates the average number of vowels in the word.
# b) Finds the word with the most vowels.
#
# *****************************************************
# PART A
# input: prompting the user for a word
word = input("Please enter a word (type 'exit' to quit): ")

# variable declaration
word = word.lower()
vowel = int(0)
total = int(0)

# process: using a while exit is not the word inputted loop to find the vowels
while word != "exit":
    for i in range(len(word)):
        if "aeiou".find(word[i]) != -1:
            vowel += 1  # if a vowel is found, + 1
    total += 1  # adding one to the total words amount
    word = input("Please enter another word (type exit to quit): ").lower()

# output: printing the average vowels in the words amount
print(f"the average vowels in all your words is {round(vowel/total, 2)} vowels per word.")
print()

# PART B
print("<<<PART B>>>")

vowel = int(0)
# input: prompting the user for a word
word = input("Please enter a word (type 'exit' to quit): ").lower()

# using for loop to find if vowels are in the word
for i in range(len(word)):
    if "aeiou".find(word[i]) != -1:
        vowel += 1  # if a vowel is found, + 1
biggest = vowel  # initializing the current most
biggest_word = word  # initializing the current word with most vowels

# process: prompting for more words and continuing to find vowels
while word != "exit":
    word = input("Please enter a word (type 'exit' to quit): ").lower()
    vowel = int(0)
    for i in range(len(word)):
        if "aeiou".find(word[i]) != -1:
            vowel += 1  # if a vowel is found, + 1
    # if the vowels in this word are more than the previous, replace both biggest and biggest_word
    if vowel > biggest:
        biggest = vowel
        biggest_word = word
    # if the vowels are the same, keep the vowel the same and add the word to biggest_word
    elif vowel == biggest:
        biggest = vowel
        biggest_word += " " + word

# output: printing the word with the most vowels
print(f"The word(s) with the most vowels is {biggest_word}.")