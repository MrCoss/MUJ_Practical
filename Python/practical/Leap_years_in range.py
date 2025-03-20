# Q-list of leap year in 2000 to 2025

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Generate list of leap years from 2000 to 2025
leap_years = [year for year in range(2000, 2026) if is_leap_year(year)]

# Print the list of leap years
print("Leap years from 2000 to 2025:", leap_years)
