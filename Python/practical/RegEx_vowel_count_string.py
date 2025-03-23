# Python program that takes custom input from the user and counts the number of vowels and consonants using regular expressions:

import re

# Function to count vowels and consonants
def count_vowels_consonants(s):
    # Convert string to lowercase for uniformity
    s = s.lower()
    
    # Regular expressions to match vowels and consonants
    vowels = re.findall(r'[aeiou]', s)  # Finds all vowels
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', s)  # Finds all consonants
    
    # Print the counts
    print(f"Number of Vowels: {len(vowels)}")
    print(f"Number of Consonants: {len(consonants)}")

# Taking user input
input_str = input("Enter a string: ")
count_vowels_consonants(input_str)
