from book_manager import add_book, view_books, update_book_status, delete_book

# Add a book
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
add_book("1984", "George Orwell", 1949)
print("Books added successfully.")

# View books
books = view_books()
print("Books in library:")
for book in books:
    print(book)

# Update book status
update_book_status(1, "borrowed")
print("Book status updated.")

# View books after update
books = view_books()
print("Updated books in library:")
for book in books:
    print(book)

# Delete a book
delete_book(1)
print("Book removed successfully.")

# View books after deletion
books = view_books()
print("Books in library after deletion:")
for book in books:
    print(book)
