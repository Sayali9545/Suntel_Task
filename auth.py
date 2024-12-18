import mysql.connector

# Database connection
def get_connection():
    return mysql.connector.connect(
        user="root",
        password="",
        host="localhost",  # Replace with your MySQL root password
        database="library_management"
    )

# Authenticate user
def authenticate(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

# Register user
def register_user(username, password, role="user"):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
        connection.commit()
        print("User registered successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
