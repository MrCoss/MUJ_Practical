# Write a Python function to generate Pascal's Triangle up to a given number of rows.

def pascal_triangle(n):
    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # Sum of two numbers above
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

# Example usage
rows = int(input("Enter the number of rows: "))
triangle = pascal_triangle(rows)

for row in triangle:
    print(" ".join(map(str, row)))  # Print each row

