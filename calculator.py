import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append text to entry widget
def append_text(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget
entry = tk.Entry(root, width=30, font=('Arial', 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and position buttons
row = 1
col = 0
for label in button_labels:
    if label == '=':
        tk.Button(root, text=label, width=10, height=2, command=evaluate_expression).grid(row=row, column=col, padx=5, pady=5)
    elif label == 'C':
        tk.Button(root, text=label, width=10, height=2, command=clear_entry).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=label, width=10, height=2, command=lambda char=label: append_text(char)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
