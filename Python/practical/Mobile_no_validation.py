# Validate an Indian Mobile Number

# Write a Python program to check if a given mobile number is valid.
# Format: 10-digit number starting with 6-9 (e.g., 9876543210)

import re

def validate_mobile(mobile):
  pattern = r'^[6-9]{1}[0-9]{9}$' #Indian Mobile format

  if re.fullmatch(pattern, mobile):
    return "Valid Mobile Number"
  else:
    return "Invalid mobile Number"
  
# Taking user input 
mobile_number = input("Enter your mobile Number: ").strip()

# Checking validity
print(validate_mobile(mobile_number))