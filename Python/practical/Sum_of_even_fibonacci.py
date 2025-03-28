# Write a Python program to find the sum of all even Fibonacci numbers up to a given limit.


def even_fibonacci_sum(limit):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    even_sum = 0  # Variable to store the sum of even Fibonacci numbers

    while b <= limit:
        if b % 2 == 0:  # Check if the number is even
            even_sum += b
        a, b = b, a + b  # Move to the next Fibonacci number

    return even_sum

# Example usage
limit = int(input("Enter the limit: "))
print("Sum of even Fibonacci numbers up to", limit, "is:", even_fibonacci_sum(limit))
