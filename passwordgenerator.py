import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate():
    username = username_entry.get()
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_var.set(f"Username: {username}\nPassword: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Username input
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Password length input
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=1, column=0, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.insert(0, "12")  # Default password length
length_entry.grid(row=1, column=1, padx=5, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Generated password display
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, wraplength=300)
password_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
