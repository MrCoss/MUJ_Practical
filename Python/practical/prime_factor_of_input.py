# Write a program to create a list of prime factors of an input number

def prime_factors(n):
  factors = [] # List to store prime factors
  divisor = 2 # Smallest prime number

  while n % divisor == 0 : # Check for factor 2 seperately
    factors.append(divisor)
    n //= divisor # Reduce n by dividing it by 2
  
  divisor = 3 # Start checking from next odd number
  while divisor * divisor <= n: # Iterate only till sqrt(n)
    while n % divisor == 0:
      factors.append(divisor)
      n //= divisor
    divisor += 2 #Increment by 2 to check only odd numbers  
  if n > 1:  # If n is still greater than 1, it is prime
      factors.append(n)
  return factors

# Example usage
number = int(input("Enter a number: "))
print(f"Prime factors of {number}: {prime_factors(number)}")  