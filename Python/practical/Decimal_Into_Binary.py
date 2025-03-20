# Write a basic python program to convert decimal into binary using recursion. Sample input:- 5 and sample output:- 101

# Function to convert decimal to binary using recursion
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

# Taking user input
num = int(input("Enter a decimal number: "))

# Handling case when input is 0
if num == 0:
    print("Binary:", 0)
else:
    print("Binary:", decimal_to_binary(num))
