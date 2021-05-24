# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 18 2021
# Program Name: lesson14_2.py
# Description: Write a program that asks the user to enter a word and
# a) Removes all vowels from the word.
# b) Replaces all vowels with ‘*’.
# c) Replaces all consonants with ‘9’.
# d) Capitalizes all vowels and makes all consonants lowercase.
# e) Replace every vowel with the next vowel.
# f) Change all letters ‘f’ to ‘F’
# g) Removes all alpha characters
# h) Removes all numbers
#
# *****************************************************
word = str()


# part a
word = input("Please enter a phrase: ").lower()
print("part a: removes all vowels. ")
for i in range(len(word)):
    if "aeiou".find(word[i]) == -1:
        print(word[i], end="")
print()
print()

# part b
print("part b: replaces all vowels with '*'.")
word = input("Please enter a word: ").lower()

for i in range(len(word)):
    if "aeiou".find(word[i]) != -1:
        print(word[i].replace(word[i], "*"), end="")
    else:
        print(word[i], end="")
print()
print()

# part c
# variable declaration
word_2 = ""
# printing part c
print("part c: replaces all consonants with ‘9’.")
word = input("Please enter a phrase: ").lower()
for i in range(len(word)):
    if word[i].isalpha and "aeiou".find(word[i]) == -1:
        word_2 += "9"
    else:
        word_2 += word[i]
print(word_2)
print()

# part d
print("part d: capitalizes all vowels and makes all consonants lowercase.")
word = input("Please enter a phrase: ").lower()
# variable declaration
word_2 = ""
# printing part d
for i in range(len(word)):
    if word[i].isalpha and "aeiou".find(word[i]) != -1:
        word_2 += word[i].upper()  # if vowels, make uppercase
    else:
        word_2 += word[i].lower()  # if no vowels, keep them lowercase
print(word_2)
print()

# part e
print("part e: replace every vowel with the next vowel.")
word = input("Please enter a phrase: ").lower()
for i in range(len(word)):
    if "aeiou".find(word[i])!=-1:
        for j in range(len("aeiou")):
            if "aeiou"[j] == word[i]:
                if j+1 < 5 or j+1 > 5 and j + 1 <= 9:
                    print("aeiou"[j+1], end="")
                else:
                    if j == 4:
                        print("a", end="")
                    else:
                        print("A", end="")
    else:
        print(word[i], end="")
print()
print()

# part f
print("part f: change all letters ‘f’ to ‘F’.")
word = input("Please enter a phrase: ").lower()
for i in range(len(word)):
    if word[i] == "f":
        print("F", end="")
    else:
        print(word[i], end="")
print()
print()

# part g
print("part g: removes all alphabet characters")
word = input("Please enter a string with any characters: ").lower()
for i in range(len(word)):
    if not word[i].isalpha():
        print(word[i], end="")
print()
print()

# part h
print("part h: removes all numbers.")
word = input("Please enter a string with any characters: ").lower()
for i in range(len(word)):
    if not word[i].isdigit():
        print(word[i], end="")
print()
print()

# closing the program
print("Thank you for using this program!!")

