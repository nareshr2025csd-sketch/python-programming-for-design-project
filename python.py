import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += "!@#$%^&*()-_=+"

    if not characters:
        messagebox.showwarning(
            "Warning", "Select at least one character type!"
        )
        return

    length = int(length_var.get())

    password = "".join(
        secrets.choice(characters) for _ in range(length)
    )

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Warning", "Generate a password first!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("440x490")
root.resizable(False, False)
root.configure(bg="#101827")

title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 19, "bold"),
    bg="#101827",
    fg="#60A5FA"
)
title.pack(pady=(25, 8))

subtitle = tk.Label(
    root,
    text="Create a strong random password",
    font=("Arial", 10),
    bg="#101827",
    fg="#CBD5E1"
)
subtitle.pack(pady=(0, 20))

password_entry = tk.Entry(
    root,
    font=("Consolas", 13),
    width=33,
    justify="center",
    state="readonly",
    readonlybackground="#243247",
    fg="#FFFFFF",
    relief="flat"
)
password_entry.pack(ipady=10, padx=20)

options_frame = tk.Frame(root, bg="#101827")
options_frame.pack(pady=18)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

def add_option(text, variable):
    tk.Checkbutton(
        options_frame,
        text=text,
        variable=variable,
        font=("Arial", 11),
        bg="#101827",
        fg="white",
        selectcolor="#243247",
        activebackground="#101827",
        activeforeground="white"
    ).pack(anchor="w", pady=3)

add_option("Uppercase letters (A-Z)", uppercase_var)
add_option("Lowercase letters (a-z)", lowercase_var)
add_option("Numbers (0-9)", numbers_var)
add_option("Symbols (!@#$...)", symbols_var)

length_var = tk.IntVar(value=16)

length_label = tk.Label(
    root,
    text="Password length: 16",
    font=("Arial", 11, "bold"),
    bg="#101827",
    fg="white"
)
length_label.pack(pady=(8, 0))

def update_length(value):
    length_label.config(text=f"Password length: {int(float(value))}")

length_slider = tk.Scale(
    root,
    from_=8,
    to=64,
    orient="horizontal",
    variable=length_var,
    command=update_length,
    bg="#101827",
    fg="white",
    troughcolor="#60A5FA",
    highlightthickness=0,
    length=300
)
length_slider.pack()

generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
generate_button.pack(fill="x", padx=45, pady=(18, 8), ipady=8)

copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 11),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
copy_button.pack(fill="x", padx=45, ipady=6)

root.mainloop()