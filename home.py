import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
from book_manager import add_book, view_books, update_book_status, delete_book

# Home Screen
def home_screen(username, role):
    def go_to_view_books():
        view_books_screen()

    def go_to_add_books():
        add_books_screen()

    def go_to_update_books():
        update_books_screen()

    def go_to_remove_books():
        remove_books_screen()

    home_window = tk.Tk()
    home_window.title("Library Management System - Home")
    home_window.geometry("800x500")

    # Load background image
    background_image = Image.open("D:\m5.jpeg")
    background_image = background_image.resize((800, 500))
    background_photo = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(home_window, width=800, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Home frame
    home_frame = tk.Frame(home_window, bg="white", padx=20, pady=20)
    home_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(home_frame, text=f"Welcome, {username}!", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    tk.Label(home_frame, text=f"Role: {role}", font=("Arial", 12), bg="white").pack(pady=5)

    tk.Button(home_frame, text="View Books", font=("Arial", 12), command=go_to_view_books, bg="#2196F3", fg="white", width=15).pack(pady=5)
    tk.Button(home_frame, text="Add Books", font=("Arial", 12), command=go_to_add_books, bg="#4CAF50", fg="white", width=15, state=("disabled" if role != "admin" else "normal")).pack(pady=5)
    tk.Button(home_frame, text="Update Books", font=("Arial", 12), command=go_to_update_books, bg="#FFC107", fg="white", width=15, state=("disabled" if role != "admin" else "normal")).pack(pady=5)
    tk.Button(home_frame, text="Remove Books", font=("Arial", 12), command=go_to_remove_books, bg="#F44336", fg="white", width=15, state=("disabled" if role != "admin" else "normal")).pack(pady=5)

    home_window.mainloop()

# Example: Add, View, Update, and Remove Books functions
def view_books_screen():
    view_window = tk.Tk()
    view_window.title("View Books")
    view_window.geometry("800x500")

    books = view_books()
    text = "\n".join([f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Status: {book[4]}" for book in books])

    tk.Label(view_window, text="Books in Library", font=("Arial", 16)).pack(pady=10)
    text_widget = tk.Text(view_window, wrap="word", height=20, width=90)
    text_widget.insert("1.0", text)
    text_widget.pack()
    text_widget.configure(state="disabled")  # Make text widget read-only

    view_window.mainloop()

# Add books screen
def add_books_screen():
    def handle_add():
        title = title_entry.get()
        author = author_entry.get()
        year = year_entry.get()
        if title and author and year.isdigit():
            add_book(title, author, int(year))
            messagebox.showinfo("Success", "Book added successfully!")
            add_window.destroy()
        else:
            messagebox.showerror("Error", "Please provide valid details.")

    add_window = tk.Tk()
    add_window.title("Add Books")
    add_window.geometry("400x300")

    tk.Label(add_window, text="Title:").pack()
    title_entry = tk.Entry(add_window)
    title_entry.pack()

    tk.Label(add_window, text="Author:").pack()
    author_entry = tk.Entry(add_window)
    author_entry.pack()

    tk.Label(add_window, text="Published Year:").pack()
    year_entry = tk.Entry(add_window)
    year_entry.pack()

    tk.Button(add_window, text="Add Book", command=handle_add).pack()

    add_window.mainloop()

# Update books screen
def update_books_screen():
    def handle_update():
        book_id = id_entry.get()
        status = status_entry.get()
        if book_id.isdigit() and status in ["available", "borrowed"]:
            update_book_status(int(book_id), status)
            messagebox.showinfo("Success", "Book status updated!")
            update_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid book ID or status.")

    update_window = tk.Tk()
    update_window.title("Update Book Status")
    update_window.geometry("400x300")

    tk.Label(update_window, text="Book ID:").pack()
    id_entry = tk.Entry(update_window)
    id_entry.pack()

    tk.Label(update_window, text="New Status (available/borrowed):").pack()
    status_entry = tk.Entry(update_window)
    status_entry.pack()

    tk.Button(update_window, text="Update Status", command=handle_update).pack()

    update_window.mainloop()

# Remove books screen
def remove_books_screen():
    def handle_remove():
        book_id = id_entry.get()
        if book_id.isdigit():
            delete_book(int(book_id))
            messagebox.showinfo("Success", "Book removed!")
            remove_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid book ID.")

    remove_window = tk.Tk()
    remove_window.title("Remove Book")
    remove_window.geometry("400x300")

    tk.Label(remove_window, text="Book ID:").pack()
    id_entry = tk.Entry(remove_window)
    id_entry.pack()

    tk.Button(remove_window, text="Remove Book", command=handle_remove).pack()

    remove_window.mainloop()
