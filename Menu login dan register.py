import csv
import os
from tkinter import Tk, Label, Entry, Button, Frame, messagebox
import tkinter as tk
from PIL import Image, ImageTk

def register():
    username = entry_register_username.get()
    password = entry_register_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Username and Password cannot be empty")
        return

    dataakun = []

    try:
        with open('dataakun.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=",")
            for row in csv_reader:
                dataakun.append({'username': row[0], 'password': row[1]})
    except FileNotFoundError:
        with open('dataakun.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['username', 'password'])
            writer.writeheader()

    username_ada = False

    for akun in dataakun:
        if username == akun['username']:
            messagebox.showwarning("Error", "Username already exists! Choose another one.")
            username_ada = True
            break

    if not username_ada:
        databaru = {'username': username, 'password': password}
        with open('dataakun.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['username', 'password'])
            writer.writerow(databaru)
        messagebox.showinfo("Success", "Registration successful")

def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Username and Password cannot be empty")
        return

    dataakun = []
    try:
        with open('dataakun.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=",")
            for row in csv_reader:
                dataakun.append({'username': row[0], 'password': row[1]})
    except FileNotFoundError:
        messagebox.showwarning("Error", "File dataakun.csv not found")
        return

    login_berhasil = False
    for akun in dataakun:
        if username == akun['username'] and password == akun['password']:
            messagebox.showinfo("Success", "Login successful")
            show_main(username)  # Arahkan ke halaman utama setelah login berhasil
            login_berhasil = True
            break

    if not login_berhasil:
        messagebox.showwarning("Error", "Account not found or incorrect password")

def show_register_frame():
    register_frame.place(x=650, y=380)
    login_frame.place_forget()
    main_frame.place_forget()

def show_login_frame():
    login_frame.place(x=650, y=380)
    register_frame.place_forget()
    main_frame.place_forget()

def show_main(username=None):
    login_frame.place_forget()
    register_frame.place_forget()
    main_frame.place(x=650, y=380)
    if username:
        welcome_label.config(text=f"Welcome, {username} to this app!")
        
# Main window
root = Tk()
root.title("Login and Registration System")
root.geometry("1200x800")

# Load and set background image
bg_image = Image.open("C:/TUBES PRAKPROK/Mencobaaa/wisata.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas with the background image
canvas = tk.Canvas(root, width=1200, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(-175, -50, image=bg_photo, anchor="nw")

# Register Frame
register_frame = Frame(root, bg="white")
Label(register_frame, text="Register", font=("Helvetica", 14), bg="white").grid(row=0, columnspan=2, pady=10)
Label(register_frame, text="Username", bg="white").grid(row=1, column=0, pady=5)
Label(register_frame, text="Password", bg="white").grid(row=2, column=0, pady=5)

entry_register_username = Entry(register_frame)
entry_register_password = Entry(register_frame, show='*')
entry_register_username.grid(row=1, column=1, pady=5)
entry_register_password.grid(row=2, column=1, pady=5)

Button(register_frame, text="Register", command=register).grid(row=3, columnspan=2, pady=10)
Button(register_frame, text="Go to Login", command=show_login_frame).grid(row=4, columnspan=2)

# Login Frame
login_frame = Frame(root, bg="white")
Label(login_frame, text="Login", font=("Helvetica", 14), bg="white").grid(row=0, columnspan=2, pady=10)
Label(login_frame, text="Username", bg="white").grid(row=1, column=0, pady=5)
Label(login_frame, text="Password", bg="white").grid(row=2, column=0, pady=5)

entry_login_username = Entry(login_frame)
entry_login_password = Entry(login_frame, show='*')
entry_login_username.grid(row=1, column=1, pady=5)
entry_login_password.grid(row=2, column=1, pady=5)

Button(login_frame, text="Login", command=login).grid(row=3, columnspan=2, pady=10)
Button(login_frame, text="Go to Register", command=show_register_frame).grid(row=4, columnspan=2)

# Main Frame
main_frame = tk.Frame(root, bg="white")
welcome_label = tk.Label(main_frame, text="Welcome to the Main Page", font=("Helvetica", 14), bg="white")
welcome_label.pack(pady=20)

info_button = tk.Button(main_frame, text="Lanjutkan", command=show_main, font=("Helvetica", 14), bg="white")
info_button.pack(pady=20)

logout_button = tk.Button(main_frame, text="Logout", command=show_login_frame, font=("Helvetica", 14), bg="red", fg="white")
logout_button.pack(pady=20)

# Initially show login frame
show_login_frame()

root.mainloop()