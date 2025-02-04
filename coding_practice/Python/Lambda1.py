# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# Add 10 to argument a, and return the result:

# OR we can say ---Anonymous functions--------
# Anonymous functions in Python are known as "lambda" functions. They are called
# "anonymous" because they are functions that are defined without a name. The syntax for a
# lambda function is as follows:
# lambda parameters: expression
# Lambda functions are particularly useful when you need a small, concise function for a
# specific task. They’re commonly used with functions like map(), filter(), and reduce().

# Example: A lambda function that returns the square of a number.
square = lambda x : x**2
print("Square of a given number is: ",square(5)) 

# You can use a lambda function to square all numbers in a list:
numbers = [1, 2, 3, 4, 5]
list_square = list(map(lambda x: x**2,numbers))
print("Square of given list",list_square)

# Multiply argument a with argument b and return the result:

multiply = lambda a,b : a*b
print("Multiplication",multiply(4,5))

# Summarize argument a, b, and c and return the result:
sum = lambda a,b,c: a+b+c
print("Sum of given numbers",sum(5,2,3))

# Given def myfunc(n):
#   return lambda a : a * n
# Use this function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a: a*n
my_doubler = myfunc(2)
print("Double of a given number is: ",my_doubler(12))

