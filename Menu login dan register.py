import tkinter as tk
from tkinter import messagebox
from tkinter import Entry, Button, Frame, Label
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import os

def register():
    username = entry_register_username.get()
    password = entry_register_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Username and Password cannot be empty")
        return

    dataakun = []
    file_path = 'dataakun.xlsx'

    if os.path.exists(file_path):
        workbook = load_workbook(file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            dataakun.append({'username': row[0], 'password': row[1]})
    else:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(['username', 'password'])
        workbook.save(file_path)

    username_ada = False

    for akun in dataakun:
        if username == akun['username']:
            messagebox.showwarning("Error", "Username already exists! Choose another one.")
            username_ada = True
            break

    if not username_ada:
        databaru = {'username': username, 'password': password}
        sheet.append([username, password])
        workbook.save(file_path)
        messagebox.showinfo("Success", "Registration successful")

def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Username and Password cannot be empty")
        return

    dataakun = []
    file_path = 'dataakun.xlsx'

    if os.path.exists(file_path):
        workbook = load_workbook(file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            dataakun.append({'username': row[0], 'password': row[1]})
    else:
        messagebox.showwarning("Error", "File dataakun.xlsx not found")
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
    register_frame.place(x=550, y=360)
    login_frame.place_forget()
    main_frame.place_forget()

def show_login_frame():
    login_frame.place(x=550, y=360)
    register_frame.place_forget()
    main_frame.place_forget()

def show_main(username=None):
    global window
    root.withdraw()  # Sembunyikan window utama
    window = tk.Toplevel(root)
    window.title("Selamat Datang")
    window.geometry("1200x800")
    window.configure(bg="White")
    window.resizable(True, True)

    new_bg_image = Image.open(r"C:\PROKOM\Tugas-Besar\Tugas-Besar\Sapa.png")
    new_bg_image = new_bg_image.resize((1200, 800), Image.Resampling.LANCZOS)
    new_photo = ImageTk.PhotoImage(new_bg_image)

    background_label = tk.Label(window, image=new_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    new_frame = Frame(window, width=350, height=100, bg="#354f00")
    new_frame.place(x=465, y=450)

    Button(new_frame, width=38, height=1, text="Lanjutkan", fg="white", bg="#57a1f8", command=halaman_utama).place(x=40, y=20)
    Button(new_frame, width=38, height=1, text="Logout", fg="white", bg="#57a1f8", command=back_login).place(x=40, y=50)

    def new_background(event=None):
        width = window.winfo_width()
        height = window.winfo_height()
        resized_image = new_bg_image.resize((width, height), Image.Resampling.LANCZOS)
        new_photo = ImageTk.PhotoImage(resized_image)
        background_label.config(image=new_photo)
        background_label.image = new_photo


    window.bind("<Configure>", new_background)
    window.mainloop()

def back_login():
    window.destroy()
    root.deiconify()  # Tampilkan kembali window utama

def update_background(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    resized_bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_bg_image)
    background_label.config(image=bg_photo)
    background_label.image = bg_photo

def halaman_utama():
    window.withdraw()
    window2 = tk.Tk()
    window2.title("login")
    window2.geometry("1200x800")
    window2.configure(bg="White")
    window2.resizable(True,True)

def balik():
    window.destroy()


# Main window
root = tk.Tk()
root.title("Login and Registration System")
root.geometry("1200x800")

# Load and set background image
bg_image = Image.open(r"C:\Tubes Sementara\wisata.png")
bg_image = bg_image.resize((1200, 800), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

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
Label(login_frame, text="LOGIN", font=("Helvetica", 14), bg="white").grid(row=0, columnspan=2, pady=10)
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

root.bind("<Configure>", update_background)

root.mainloop()
