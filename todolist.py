import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.listbox = tk.Listbox(master, width=50)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=5, pady=5)

        self.populate_listbox()

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.populate_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            del self.tasks[task_index]
            self.populate_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[task_index] = updated_task
                self.populate_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
