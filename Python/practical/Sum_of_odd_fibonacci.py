# Python program to find the sum of all odd Fibonacci numbers up to a given limit

def sum_odd_fibonacci(limit):
    a, b = 0, 1  # First two Fibonacci numbers
    sum_odd = 0  # Variable to store sum of odd Fibonacci numbers

    while a <= limit:
        if a % 2 != 0:  # Check if Fibonacci number is odd
            sum_odd += a
        a, b = b, a + b  # Move to the next Fibonacci number
    
    return sum_odd

# Example usage:
limit = int(input("Enter the limit: "))
print("Sum of odd Fibonacci numbers up to", limit, ":", sum_odd_fibonacci(limit))
