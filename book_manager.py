import mysql.connector

# Database connection function
def get_connection():
    return mysql.connector.connect(
        user="root",
        password="",  # Replace with your MySQL root password
        host="localhost",
        database="library_management"
    )

# Add a new book
def add_book(title, author, published_year):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)"
    values = (title, author, published_year)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

# View all books
def view_books():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

# Update a book's status
def update_book_status(book_id, new_status):
    connection = get_connection()
    cursor = connection.cursor()
    query = "UPDATE books SET status = %s WHERE id = %s"
    values = (new_status, book_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

# Delete a book
def delete_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM books WHERE id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
