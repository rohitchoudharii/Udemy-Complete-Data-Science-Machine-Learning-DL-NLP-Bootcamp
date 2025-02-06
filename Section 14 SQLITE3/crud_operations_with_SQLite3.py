import sqlite3

## COnnect to a SQLite database

connection = sqlite3.connect("example.db")
print(connection)

cursor = connection.cursor()

# Create Table
cursor.execute("""
               Create Table If Not Exists employees(
                   id Integer Primary Key,
                   name test Not Null,
                   age Integer,
                   department text
               )
               """)

connection.commit()

# Create Insert queries
cursor.execute("""
               Insert into employees(name, age, department)
               VALUES ('Karan', 25, 'Director')
               """)


cursor.execute("""
               Insert into employees(name, age, department)
               VALUES ('Rohan', 25, 'Dance')
               """)

cursor.execute("""
               Insert into employees(name, age, department)
               VALUES ('Manoj', 25, 'Sales manager')
               """)

connection.commit()

# Select table

cursor.execute("""
               Select * from employees
               """)
rows = cursor.fetchall()

for row in rows:
    print(row)

# Update data in table
cursor.execute("""
               UPDATE employees
               SET age = 55
               where name = 'Rohan'
               """)

connection.commit()

# Delete data from table

cursor.execute("""
               DELETE from employees where name='Rohan'
               """)

connection.commit()

# Working with sales data
cursor.execute("""
               CREATE TABLE IF NOT EXISTS sales(
                   id INTEGER PRIMARY KEY,
                   date TEXT NOT NULL,
                   product TEXT NOT NULL,
                   sales INTEGER,
                   region TEXT
               )
               """)

connection.commit()

sales_data = [
    ("2023-01-01", "Product 1", 100, "North"),
    ("2023-01-02", "Product 2", 200, "South"),
    ("2023-01-03", "Product 3", 150, "East"),
    ("2023-01-04", "Product 4", 250, "West"),
    ("2023-01-05", "Product 5", 1000, "North"),
]

cursor.executemany(
    """
                   inser into sales(date, product, sales, refion)
                   values(?,?,?,?)
                   """,
    sales_data,
)
connection.commit()


# Select table

cursor.execute("""
               Select * from sales
               """)
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
