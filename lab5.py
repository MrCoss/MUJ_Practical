# Function to convert decimal to binary using recursion
def decimal_to_binary(decimal_number):
    # Base case: If the number is 0, return "0"
    if decimal_number == 0:
        return "0"
    else:
        # Recursively call the function to process the next digit
        result = decimal_to_binary(decimal_number // 2)
        # If the recursion reaches the base case, return "0" to prevent empty string
        if decimal_number == 0:
            return result
        else:
            return result + str(decimal_number % 2)

# Main function to handle the input and output
def main():
    # Prompt the user to enter a decimal number
    decimal_number = int(input())  # Reading input
    
    # Call the recursive function and print the result
    binary_result = decimal_to_binary(decimal_number)
    
    # Print binary result, excluding the leading "0" when input is zero
    print(binary_result)

# Call the main function to run the program
if __name__ == "__main__":
    main()
