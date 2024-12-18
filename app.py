import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from home import home_screen

# Validate credentials from the database
def validate_login(username, password):
    try:
        connection = mysql.connector.connect(
            user="root",
            password="",  # Replace with your MySQL root password
            host="localhost",
            database="library_management"
        )
        cursor = connection.cursor()
        query = "SELECT role FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        connection.close()
        return result  # Returns the role if the user exists, otherwise None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Login Screen
def login_screen():
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        user_role = validate_login(username, password)

        if user_role:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            login_window.destroy()
            home_screen(username, user_role[0])  # Pass username and role to the home page
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    login_window = tk.Tk()
    login_window.title("Library Management System - Login")
    login_window.geometry("800x500")

    # Load background image
    background_image = Image.open("D:\\istockphoto.jpg")
    background_image = background_image.resize((800, 500))
    background_photo = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(login_window, width=800, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Login frame
    login_frame = tk.Frame(login_window, bg="white", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(login_frame, text="Login", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
    tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="white").pack(pady=5)
    username_entry = tk.Entry(login_frame, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="white").pack(pady=5)
    password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    tk.Button(login_frame, text="Login", font=("Arial", 12), command=handle_login, bg="#4CAF50", fg="white", width=10).pack(pady=10)

    login_window.mainloop()

if __name__ == "__main__":
    login_screen()
