# Write a lambda function to check whether a given number is positive, negative, or zero.

y = float(input())  # Convert input to a number (float or int)
check_x = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check_x(y))


# Create a lambda function to find the square of a given number.

square = lambda a: a**2
print("square of given number is : ",square(5))