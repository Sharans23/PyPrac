import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def register_user():
    username = register_username.get()
    password = register_password.get()

    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Registration", "Registration Successful!")

def login_user():
    username = login_username.get()
    password = login_password.get()

    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

# GUI setup
root = tk.Tk()
root.title("Login and Register")

# Register Page
register_frame = tk.Frame(root)
register_frame.pack(pady=10)

register_label = tk.Label(register_frame, text="Register", font=("Helvetica", 16))
register_label.grid(row=0, column=0, columnspan=2, pady=10)

register_username_label = tk.Label(register_frame, text="Username:")
register_username_label.grid(row=1, column=0)
register_username = tk.Entry(register_frame)
register_username.grid(row=1, column=1)

register_password_label = tk.Label(register_frame, text="Password:")
register_password_label.grid(row=2, column=0)
register_password = tk.Entry(register_frame, show="*")
register_password.grid(row=2, column=1)

register_button = tk.Button(register_frame, text="Register", command=register_user)
register_button.grid(row=3, column=0, columnspan=2, pady=10)

# Login Page
login_frame = tk.Frame(root)
login_frame.pack(pady=10)

login_label = tk.Label(login_frame, text="Login", font=("Helvetica", 16))
login_label.grid(row=0, column=0, columnspan=2, pady=10)

login_username_label = tk.Label(login_frame, text="Username:")
login_username_label.grid(row=1, column=0)
login_username = tk.Entry(login_frame)
login_username.grid(row=1, column=1)

login_password_label = tk.Label(login_frame, text="Password:")
login_password_label.grid(row=2, column=0)
login_password = tk.Entry(login_frame, show="*")
login_password.grid(row=2, column=1)

login_button = tk.Button(login_frame, text="Login", command=login_user)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Initialize the database table
create_table()

root.mainloop()