# Write a Python program to find the LCM (Least Common Multiple) of two numbers.
import math

# Function to find LCM
def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)  # Using GCD to find LCM, math.gcd(a, b) finds the Greatest Common Divisor (GCD).
    # abs(a * b) // gcd(a, b) calculates and returns the LCM.

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculating LCM
lcm = find_lcm(num1, num2)

# Displaying result
print(f"The LCM of {num1} and {num2} is {lcm}")

