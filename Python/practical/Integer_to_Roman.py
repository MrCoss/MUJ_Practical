# Write a Python function to convert an integer to Roman numerals.

def int_to_roman(num):
    # Mapping of integer values to Roman numeral symbols
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_string = ""  # To store the result

    for value, symbol in roman_numerals:
        while num >= value:
            roman_string += symbol
            num -= value  # Subtract the value from the number
    
    return roman_string  # Return the final Roman numeral representation

# Example usage
number = int(input("Enter an integer: "))
print(f"Roman numeral: {int_to_roman(number)}")

