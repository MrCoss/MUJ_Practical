# Write a Python program to print the first 10 Fibonacci numbers in reverse order

def fibonacci_reverse(n):
    fib_sequence = [0, 1]  # Initialize list with first two Fibonacci numbers
    
    # Generate first n Fibonacci numbers
    for _ in range(n - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Print in reverse order
    for num in reversed(fib_sequence):
        print(num, end=" ")

# Print first 10 Fibonacci numbers in reverse order
fibonacci_reverse(10)
