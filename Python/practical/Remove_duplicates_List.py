# Write a Python program to remove duplicates from a given list.

def remove_duplicates(lst):
    return list(set(lst))  # Convert list to set to remove duplicates, then back to list

# Example usage
my_list = list(map(int, input("Enter numbers separated by space: ").split()))
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)

