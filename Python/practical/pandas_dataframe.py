# Write a Python program that creates a Pandas DataFrame from the given dictionary and drops rows with missing values
# data_dict = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
#     'Age': [25, 30, None, 45, 50],
#     'City': ['New York', None, 'Los Angeles', 'Chicago', 'Houston']
# }

import pandas as pd

# Dictionary containing the data with missing values
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, 30, None, 45, 50],
    'City': ['New York', None, 'Los Angeles', 'Chicago', 'Houston']
}

# Create DataFrame from dictionary
df = pd.DataFrame(data_dict)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Drop rows with any missing values
df_cleaned = df.dropna()

# Display cleaned DataFrame
print("\nDataFrame after dropping rows with missing values:")
print(df_cleaned)