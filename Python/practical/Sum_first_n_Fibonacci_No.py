# Calculates the sum of the first n Fibonacci numbers.
def fibonacci_sum(n):
  """
  Calculates the sum of the first n Fibonacci numbers.

  Args:
    n: The number of Fibonacci numbers to sum.

  Returns:
    The sum of the first n Fibonacci numbers.
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    fib_list = [0, 1]
    for i in range(2, n):
      fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return sum(fib_list)

# Example usage:
n = 10
result = fibonacci_sum(n)
print(result)
# for n = 10, output 88