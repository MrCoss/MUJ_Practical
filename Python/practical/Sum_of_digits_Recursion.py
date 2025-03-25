# Write a Python program to find the sum of digits of a given number using recursion.

def sum_of_digits(n):
    if n == 0:  # Base case: If the number is 0, return 0
        return 0
    return (n % 10) + sum_of_digits(n // 10)  # Add last digit to sum of remaining digits

# Example usage
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits:", result)

