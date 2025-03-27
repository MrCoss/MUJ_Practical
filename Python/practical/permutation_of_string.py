# Write a Python program to find all the permutations of a given string using recursion.

def permute(string, step=0):
    # Base Case: If we reached the end of the string, print the permutation
    if step == len(string):
        print("".join(string))
        return

    for i in range(step, len(string)):
        # Swap the current index with the step
        string_list = list(string)
        string_list[step], string_list[i] = string_list[i], string_list[step]

        # Recur with the next step
        permute(string_list, step + 1)

# Input string
string = "ABC"

# Call the function
permute(string)

