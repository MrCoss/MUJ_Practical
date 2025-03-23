# Write a Python program to create a dictionary having keys upper_case, lower_case,digits,spaces,and special_symbol as keys and its count in the given string.

# Given String input
# Str1 = "Hello all, I am Aman Sharma. My ID is aman@0702@gmail.com"
Str1 = "Hi, I am Jay. My ID is jay@07"

# Initilitialize counters
upper_case_count = 0
lower_case_count = 0
digit_count = 0
space_count = 0
special_symbol_count = 0


for char in Str1:
  if char.isupper():
    upper_case_count += 1
  elif char.islower():
    lower_case_count += 1
  elif char.isdigit():
    digit_count += 1    
  elif char.isspace():
    space_count += 1
  else:
    special_symbol_count += 1

  # Create a dictionary to store the counts
count_dict = {
    'upper_case': upper_case_count,
    'lower_case': lower_case_count,
    'digits': digit_count,
    'spaces': space_count,
    'special_symbol': special_symbol_count
  }

print(count_dict)      