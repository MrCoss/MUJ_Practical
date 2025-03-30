# Python program to replace "JAVA" with "PYTHON" in the given string using the re.sub() method
# str1 = "JAVA IS AN OBJECT-ORIENTED PROGRAMMING LANGUAGE."


import re

# Given string
str1 = "JAVA IS AN OBJECT-ORIENTED PROGRAMMING LANGUAGE."

# Using re.sub() to replace "JAVA" with "PYTHON"
updated_str = re.sub(r'\bJAVA\b', 'PYTHON', str1)  # r'\bJAVA\b': The \b ensures that we replace only the whole word "JAVA" (not part of another word).

# Display the result
print("Updated String:", updated_str)

