# Use a lambda function inside filter() to extract only palindromic words from a given list of words.

# A palindromic word is a word that reads the same forward and backward. This means that if you reverse the order of its letters, you get the same word.

# Examples of Palindromic Words
# ✅ madam → Reverse → madam
# ✅ racecar → Reverse → racecar
# ✅ level → Reverse → level
# ✅ refer → Reverse → refer



list1=["apple","madam","level","mango"]
pelindrome_check = filter(lambda words: words==words[::-1],list1)
print(list(pelindrome_check))


# The filter() function in Python is used to filter elements from an iterable (like a list, tuple, or string) based on a condition defined by a function (usually a lambda function). It constructs a new iterator that includes only the items that satisfy the condition (i.e., return True).

# Syntax:
# filter(function, iterable)
# function: A function that tests each element of the iterable. It should return True or False.
# iterable: Any iterable (e.g., list, tuple, etc.) whose elements will be tested by the function.
# The filter() function returns an iterator (not a list). To see the results, you often need to convert the iterator to a list, tuple, etc.

# Basic Example:
# Let's say we want to filter out even numbers from a list:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)

# # Convert filter object to list and print
# print(list(even_numbers))  # Output: [2, 4, 6, 8]
# How it Works:
# lambda x: x % 2 == 0: This is the condition for filtering. It checks if the number is even.
# filter() applies this condition to each element in the numbers list, and the resulting iterator contains only the numbers that satisfy the condition (even numbers).
