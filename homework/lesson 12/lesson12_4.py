# *****************************************************
#
# Program Author: Frances Zhao
# Completion Date: May 18 2021
# Program Name: lesson12_4.py
# Description: Gather a word from the user and display
# 1. its letters one per line.
# 2. its letters in reverse order, one per line.
# 3. it with its first and last letters exchanged.
# 4. it with its first half exchanged with its second half.
# 5. it with every letter ‘d’ replaced with a D
# 6. it with every letter ‘a’ removed
#
# *****************************************************

# variable declaration
word = str()

# input: prompting the user for a word
word = input("Please input a word: ")

# part 1: displaying letters one per line
for character in word:
    print(character)
print()

# part 2: displaying letters backwards one per line
for character in word[::-1]:
    print(character)
print()


# part 3: swapping the first and last letters of the word
def swap(word):
    first_letter = word[0]
    last_letter = word[-1]
    word_swap = last_letter + word[1:-1] + first_letter
    return word_swap


print(swap(word))
print()

# part 4: cutting the word in half and printing the second half first
first_half = word[:len(word)//2]
second_half = word[len(word)//2:]
print(f"{second_half}{first_half}")
print()

# part 5: replacing the letter "d" with "D" if applies
replace = word.replace("d", "D")
print(replace)
print()

# part 6: removing the letter "a" if applies
remove = word.replace("a", "")
print(remove)