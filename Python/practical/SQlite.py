# Write a Python program in SQLite with the following instructions:

# Create a database named STUDENTS.

# Create a table named STU_DETAILS with the following fields:

# STU_ID (Integer, Primary Key)

# NAME (Text, Not Null)

# BRANCH (Text, Not Null)

# Insert data of three students into the table:

# (101, "Aman", "CS")

# (102, "Vimal", "ECE")

# (103, "Rohit", "ECE")

# Update the BRANCH of the student having STU_ID = 103 to "ME".


import sqlite3

# Step 1: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Step 2: Create the STUDENTS table
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS (
                    STU_ID INTEGER PRIMARY KEY,
                    NAME TEXT NOT NULL,
                    BRANCH TEXT NOT NULL)''')

# Step 3: Insert data for 3 students
cursor.execute("INSERT INTO STUDENTS (STU_ID, NAME, BRANCH) VALUES (101, 'Aman', 'CS')")
cursor.execute("INSERT INTO STUDENTS (STU_ID, NAME, BRANCH) VALUES (102, 'Vimal', 'ECE')")
cursor.execute("INSERT INTO STUDENTS (STU_ID, NAME, BRANCH) VALUES (103, 'Rohit', 'ECE')")

# Commit the changes
conn.commit()

# Step 4: Update the BRANCH of the student with STU_ID 103 to 'ME'
cursor.execute("UPDATE STUDENTS SET BRANCH = 'ME' WHERE STU_ID = 103")

# Commit the changes
conn.commit()

# Step 5: Fetch and print the updated row
cursor.execute("SELECT * FROM STUDENTS WHERE STU_ID = 103")
updated_row = cursor.fetchone()
print("Updated Row:", updated_row)

# Close the connection
conn.close()

