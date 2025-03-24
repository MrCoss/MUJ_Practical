# Write a Python program to check if a given number is an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153).

def is_armstrong(number):
    digits = list(map(int, str(number)))  # Convert number to a list of digits
    power = len(digits)  # Get the number of digits
    armstrong_sum = sum(d ** power for d in digits)  # Compute the sum of digits raised to the power
    return armstrong_sum == number  # Check if the sum matches the original number

# Example usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

