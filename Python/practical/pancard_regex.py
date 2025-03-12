# Write a python program to validate input PAN number using a regular expression 
# PAN Format:
# PAN is a 10-character alphanumeric identifier.
# The format is: AAAAA9999A, where:
# First 5 characters → Uppercase letters (A-Z).
# Next 4 characters → Digits (0-9).
# Last 1 character → Uppercase letter (A-Z).

import re

def validate_pan(pan):
  pattern = r'[A-Z]{5}[0-9]{4}[A-Z]$' # Pan format regex
  if re.fullmatch(pattern, pan):
    return "Valid PAN Number"
  else:
    return "Invalid Pan Number"
  
# Taking user input
pan_number = input ("Enter your Pan Number: ").strip()

# Checking Validity
print(validate_pan(pan_number))