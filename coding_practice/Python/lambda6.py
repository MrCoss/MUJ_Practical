# Write a lambda function to generate a Fibonacci sequence up to a given number using reduce().

from functools import reduce

# Function to generate Fibonacci sequence
fibonacci = lambda n: reduce (lambda seq,_:seq+[seq[-2]+seq[-1]], range(n-2),[0,1])

n = 10
print(fibonacci(n))

# Step-by-Step Breakdown:
# reduce(function, iterable, initial):

# reduce() is a function from the functools module that takes three arguments:
# function: A function that gets applied to the items of the iterable.
# iterable: The sequence of values that the function operates on.
# initial: An optional value that initializes the sequence. In this case, [0, 1] is used as the starting list.

# Lambda Function (lambda seq, _ : seq + [seq[-2] + seq[-1]]):

# This lambda function is the core of the sequence generation.
# Parameters:
# seq: This represents the accumulated list of Fibonacci numbers so far.
# _: This represents each element of the iterable (the range(n-2)), but we don't use it in the lambda function, so we name it _ to indicate it is unused.
# The lambda function performs the following operation:
# seq + [seq[-2] + seq[-1]]: This adds a new number to the seq list. The new number is the sum of the last two elements of seq (seq[-2] and seq[-1]).
# seq[-2] refers to the second-to-last element of the list, and seq[-1] refers to the last element of the list