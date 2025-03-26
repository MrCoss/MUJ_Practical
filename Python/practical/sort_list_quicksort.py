# Write a Python program to sort a list using the QuickSort algorithm.

def quicksort(arr):
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 elements, return as it is already sorted
        return arr
    
    pivot = arr[len(arr) // 2]  # Selecting the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    
    return quicksort(left) + middle + quicksort(right)  # Recursively sort and combine

# Example Usage
arr = [34, 7, 23, 32, 5, 62, 32]
sorted_arr = quicksort(arr)
print("Sorted List:", sorted_arr)


# Explanation
# Choosing a Pivot: The middle element is chosen as the pivot to ensure a balanced partition.

# Partitioning: The list is divided into:

# Left sublist (elements smaller than pivot)

# Middle sublist (equal to pivot)

# Right sublist (greater than pivot)

# Recursive Sorting: The left and right sublists are sorted recursively.

# Merging: Finally, all parts are merged to get a sorted list.

# Why Use QuickSort?
# Fast for large datasets

# Efficient for in-memory sorting

# Commonly used in system libraries


# Tree Representation of QuickSort

# Original: [34, 7, 23, 32, 5, 62, 32]
#                       (32)
#            ┌───────────┴───────────┐
#         [7, 23, 5]             [34, 62]
#           (23)                    (62)
#         ┌───┴───┐                ┌──┴──┐
#       [7, 5]   []             [34]    []
#         (5)
#       ┌──┴──┐
#      []    [7]

# Final Merge: [5, 7, 23] + [32, 32] + [34, 62]
# Sorted List: [5, 7, 23, 32, 32, 34, 62]

