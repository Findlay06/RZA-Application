# Imports, will allow for SQL code to be executed
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("users.db") # Connects to the users database
cursor = conn.cursor() # Connects the cursor instance to use methods from sqlite, this includes fecthing data from result sets of queries

def search_data(id, name, surname, username, password, email, city, age): # This is a function for the users table as well as columns which are set as parameters 
    cursor.execute('CREATE TABLE users(id n(5), name char (30), surname char (30), username char (30), password char (30), email char (30), city char (35), age decimal(7,2));') # Creates the users table and columns
    cursor.execute("INSERT INTO users VALUES (1, 'Ryan', 'Hyde', 'HydeIO', 'FS', 'hyde25@test.com', 'London', 25)") # Inserts values into the users table and relevant columns
    cursor.execute("INSERT INTO users VALUES (2, 'Ryan', 'Lo', 'Jade', 'Vader', 'ryan54@test.com', 'Middlesbrough', 30)")
    cursor.execute("INSERT INTO users VALUES (3, 'Ryan', 'Bell', 'SDR', 'IO', 'ryan75@test.com', 'Middlesbrough', 20)")
    cursor.execute("INSERT INTO users VALUES (4, 'Hannah', 'Gray', 'JUI', 'XYZ', 'hannah24@test.com', 'London', 24)")
    cursor.execute("INSERT INTO users VALUES (5, 'Mike', 'Parker', 'GDF', 'HOL', 'mike78@test.com', 'Birmingham', 31)")
    cursor.execute("INSERT INTO users VALUES (6, 'Aaron', 'Flynn', 'FAQ', 'HK', 'flynn45@test.com', 'London', 21)")
    cursor.execute("INSERT INTO users VALUES (7, 'Clyde', 'James', 'J', 'DSA', 'clyde31@test.com', 'Birmingham', 40)")
    cursor.execute("INSERT INTO users VALUES (8, 'Christina', 'Watson', 'SAD', 'HTS', 'christina98@test.com', 'London', 25)")
    cursor.execute("INSERT INTO users VALUES (9, 'Alex', 'Carrol', 'Tao', 'HJ', 'alex67@test.com', 'Birmingham', 42)")
    cursor.execute("INSERT INTO users VALUES (7, 'Daniel', 'Mccain', 'TERMINATOR', 'NumOne', 'dan77@test.com', 'Middlesbrough, 20)")
    cursor.execute(""" 
                   INSERT INTO users(user_id, name, surname, city, age)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   """, (id, name, surname, username, password, email, city, age)) # This is to ensure all parameters are set as columns in the database 
    rows = cursor.execute("SELECT id, name, surname, username, password, email, city, age FROM user").fetchall() # Fetches all columns in the users database 
    conn.commit() # Commits to changes
    print('Data entered!')
    conn.close() # Closes the database connection
    print(rows)
    if (conn):
        conn.close()
        print('\nDatabase closed.')
    search_data(1, 'Ryan', 'Hyde', 'Ryan Hyde', 'HydeIO', 'FS', 'hyde25@test.com', 'London', 25) # Searches for the data selected in the database
