# Create a dictionary where each number from 1 to 5 is mapped to its cube!
# Method 1 BEST APPROACH
# Using Dictionary comprehension method
cubes = {num: num ** 3 for num in range(1, 6)}
print(cubes)


# Using a Loop (Traditional Approach)
cubes = {}
for num in range(1, 6):
    cubes[num] = num ** 3
print(cubes)

#Pros: Easy to understand for beginners.
#Cons: More lines of code compared to dictionary comprehension.