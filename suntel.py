import mysql.connector

# Create Database and Tables
def create_database_and_tables():
    connection = mysql.connector.connect(
        user="root",
        password="",  # Replace with your MySQL root password
        host="localhost"
    )
    cursor = connection.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_management")
    cursor.execute("USE library_management")

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        role ENUM('user', 'admin') DEFAULT 'user'
    )
    ''')

    # Create books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        status ENUM('available', 'borrowed') DEFAULT 'available',
        published_year INT NOT NULL
    )
    ''')

    connection.commit()
    cursor.close()
    connection.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database_and_tables()
import mysql.connector

# Create Database and Tables
def create_database_and_tables():
    connection = mysql.connector.connect(
        user="root",
        password="",  # Replace with your MySQL root password
        host="localhost"
    )
    cursor = connection.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_management")
    cursor.execute("USE library_management")

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        role ENUM('user', 'admin') DEFAULT 'user'
    )
    ''')

    # Create books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        status ENUM('available', 'borrowed') DEFAULT 'available',
        published_year INT NOT NULL
    )
    ''')

    connection.commit()
    cursor.close()
    connection.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database_and_tables()
