# Validate an Aadhaar Number

# Write a Python program to check if a given Aadhaar number (Indian Unique Identification Number) is valid.
# Format: 12 digits (e.g., 123456789012)

import re

def validate_aadhar(aadhar):
  pattern = r'[0-9]{12}$' #Aadhar format

  if re.fullmatch(pattern, aadhar):
    return "Valid Aadhar Number"
  else:
    return "Invalid Aadhar Number"
  
# Taking user input 
aadhar_number = input("Enter your Aadhar Number: ").strip()

# Checking validity
print(validate_aadhar(aadhar_number))