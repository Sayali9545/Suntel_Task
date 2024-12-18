import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import bcrypt

# Function to add a new user to the database
def add_new_user(username, password, role):
    try:
        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Connect to the database
        connection = mysql.connector.connect(
            user="root",
            password="",  # Replace with your MySQL root password
            host="localhost",
            database="library_management"
        )
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists.")
            connection.close()
            return

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                       (username, hashed_password, role))
        connection.commit()
        connection.close()

        # Show success message
        messagebox.showinfo("Success", f"New {role} registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        print(err)

# Admin Registration Page
def admin_registration_page():
    def handle_registration():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        role = role_var.get()

        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Add new user to the database
        add_new_user(username, password, role)

    # Create window
    reg_window = tk.Tk()
    reg_window.title("Admin Registration")
    reg_window.geometry("800x500")

    # Load background image
    background_image = Image.open("D:\\tropical-nature-bright-blue-morpho-butterfly.jpg")  # Path to your background image
    background_image = background_image.resize((800, 500))
    background_photo = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(reg_window, width=800, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Registration form frame
    reg_frame = tk.Frame(reg_window, bg="white", padx=20, pady=20)
    reg_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    tk.Label(reg_frame, text="Admin Registration", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    # Username label and entry
    tk.Label(reg_frame, text="Username:", font=("Arial", 12), bg="white").pack(pady=5)
    username_entry = tk.Entry(reg_frame, font=("Arial", 12))
    username_entry.pack(pady=5)

    # Password label and entry
    tk.Label(reg_frame, text="Password:", font=("Arial", 12), bg="white").pack(pady=5)
    password_entry = tk.Entry(reg_frame, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    # Confirm Password label and entry
    tk.Label(reg_frame, text="Confirm Password:", font=("Arial", 12), bg="white").pack(pady=5)
    confirm_password_entry = tk.Entry(reg_frame, show="*", font=("Arial", 12))
    confirm_password_entry.pack(pady=5)

    # Role selection (Admin or User)
    tk.Label(reg_frame, text="Role:", font=("Arial", 12), bg="white").pack(pady=5)
    role_var = tk.StringVar()
    role_var.set("admin")  # Default to admin
    role_menu = tk.OptionMenu(reg_frame, role_var, "admin", "user")
    role_menu.config(font=("Arial", 12))
    role_menu.pack(pady=5)

    # Register button
    register_button = tk.Button(reg_frame, text="Register", font=("Arial", 12), command=handle_registration, bg="#4CAF50", fg="white", width=15)
    register_button.pack(pady=10)

    reg_window.mainloop()

if __name__ == "__main__":
    admin_registration_page()
