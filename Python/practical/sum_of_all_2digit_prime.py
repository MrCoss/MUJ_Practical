# Write a program to calculate the sum of all 2 digit prime number
def is_prime(n):
    """Function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Calculate the sum of all two-digit prime numbers (from 10 to 99)
sum_of_primes = sum(num for num in range(10, 100) if is_prime(num))

print("Sum of all two-digit prime numbers:", sum_of_primes)
