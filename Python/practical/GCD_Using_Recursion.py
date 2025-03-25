# Write a Python program to find the greatest common divisor (GCD) of two numbers using recursion.

def gcd(a, b):
    if b == 0:  # Base case: If second number is 0, return the first number
        return a
    return gcd(b, a % b)  # Recursive call with (b, remainder of a divided by b)

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", result)

