# Write a Python program to find the second largest and second smallest elements in a list:

def second_largest_smallest(lst):
    # Remove duplicates and sort the list
    unique_lst = sorted(set(lst))
    
    # Check if list has at least two unique elements
    if len(unique_lst) < 2:
        print("Not enough unique elements to find second largest and second smallest.")
        return
    
    # Get second smallest and second largest elements
    second_smallest = unique_lst[1]
    second_largest = unique_lst[-2]

    print(f"Second Smallest: {second_smallest}")
    print(f"Second Largest: {second_largest}")

# Taking user input
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
number = []
n = int(input("Enter element size"))
for i in range(n):
    number.append(int(input(f"Enter elements of size {n}: ")))
second_largest_smallest(number)
