# Write a Python program to find the Fibonacci series using recursion
def fibonacci(n):
    # Base cases
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Recursively calculate the Fibonacci number by summing the previous two terms
        return fibonacci(n - 1) + fibonacci(n - 2)

# Taking user input
terms = int(input("Enter the number of terms: "))

# Printing Fibonacci series
print("Fibonacci Series:")
for i in range(1, terms + 1):
    print(fibonacci(i), end=" ")

# Note: The Fibonacci sequence follows the rule: F(n)=F(n−1)+F(n−2)    

