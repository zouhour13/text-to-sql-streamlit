import sqlite3

# Database setup
connection = sqlite3.connect("company.db")

# Create cursor
cursor = connection.cursor()

# Create the table for employees
create_table_query = """
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EMP_ID      INT,
    NAME        VARCHAR(25),
    DEPARTMENT  VARCHAR(25),
    POSITION    VARCHAR(25),
    SALARY      INT,
    BONUS       INT
);
"""

cursor.execute(create_table_query)

# Insert Records
sql_query = """INSERT INTO EMPLOYEE (EMP_ID, NAME, DEPARTMENT, POSITION, SALARY, BONUS) VALUES (?, ?, ?, ?, ?, ?)"""
values = [
    (101, 'Alice', 'IT', 'Developer', 6000, 500),
    (102, 'Bob', 'IT', 'Tester', 5500, 300),
    (103, 'Charlie', 'HR', 'Recruiter', 5000, 200),
    (104, 'David', 'Finance', 'Analyst', 6500, 700),
    (105, 'Eva', 'Finance', 'Manager', 8000, 1000),
    (106, 'Frank', 'IT', 'Developer', 6200, 400),
    (107, 'Grace', 'HR', 'Coordinator', 4800, 150),
    (108, 'Hannah', 'Marketing', 'Executive', 5300, 300),
    (109, 'Ian', 'Marketing', 'Manager', 7500, 600),
    (110, 'Jack', 'IT', 'Team Lead', 9000, 1000)
]

cursor.executemany(sql_query, values)
connection.commit()

# Display the records
data = cursor.execute("""SELECT * FROM EMPLOYEE""")
for row in data:
    print(row)

# Close the connection
if connection:
    connection.close()
