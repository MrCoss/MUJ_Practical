# Write a python program to create a dictionary from a given list and invert a created dictionary (Swap keys and values).
# List = [(1, "Hello"), (2,"Java"), (3,"Python")]

# Given list of tuples
data_list = [(1, "Hello"), (2, "Java"), (3, "Python")]

# Creating a dictionary from the list
data_dict = dict(data_list)
print("Original Dictionary:", data_dict)

# Inverting the dictionary (Swapping keys and values)
inverted_dict = {value: key for key, value in data_dict.items()}
print("Inverted Dictionary:", inverted_dict)

# Note:- Swap keys and values using dictionary comprehension:
# {value: key for key, value in data_dict.items()}