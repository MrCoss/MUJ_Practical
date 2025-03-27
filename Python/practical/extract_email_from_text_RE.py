# Python script to extract email addresses from a given text string using regular expressions.

import re  # Importing the regular expression module

# Given text string containing email addresses
text = "Contact us at support@example.com and sales@company.org for more info."

# Regular expression pattern to find email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Using re.findall() to extract all email addresses from the text
emails = re.findall(email_pattern, text)

# Printing the extracted email addresses
print("Extracted Email Addresses:", emails)




# Explaination
# Creating a Regular Expression Pattern (email_pattern)

# The pattern r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' is used to match email addresses.

# Breakdown of the pattern:

# [a-zA-Z0-9._%+-]+ → Matches the username part of the email (before @).

# @ → Matches the @ symbol.

# [a-zA-Z0-9.-]+ → Matches the domain name.

# \.[a-zA-Z]{2,} → Matches the dot (.) followed by at least two letters (TLD like .com, .org).

# Extracting Emails with re.findall()

# re.findall(email_pattern, text) finds all occurrences of the email pattern in the given string.

