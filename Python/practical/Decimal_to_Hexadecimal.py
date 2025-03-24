# Write a Python function to convert a number from decimal to hexadecimal.

def decimal_to_hexadecimal(n):
    return hex(n)[2:].upper()  # Convert to hex and remove '0x' prefix

# Example usage
num = int(input("Enter a decimal number: "))
hex_value = decimal_to_hexadecimal(num)
print("Hexadecimal:", hex_value)
