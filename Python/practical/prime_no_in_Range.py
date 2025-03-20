# Q-Python program to print prime numbers in any given range:

# Function to check if a number is prime
start_range = 2
end_range = 400
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to print prime numbers in a given range
def print_primes(start, end):
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")

# Example usage
# start_range = int(input("Enter start range: "))
# end_range = int(input("Enter end range: "))
print_primes(start_range, end_range)
