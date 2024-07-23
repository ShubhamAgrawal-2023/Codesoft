import tkinter as tk
import pickle  # For saving/loading tasks

# Global variables
tasks = []
completed_tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)  # Clear entry field

def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_to_delete = tasks[selected_task_index[0]]
        tasks.remove(task_to_delete)
        update_task_list()

def mark_complete():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_to_mark = tasks[selected_task_index[0]]
        tasks.remove(task_to_mark)
        completed_tasks.append(task_to_mark)
        update_task_list()

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)
    completed_list.delete(0, tk.END)
    for task in completed_tasks:
        completed_list.insert(tk.END, task + " (Completed)")  # Mark completed tasks

def save_tasks():
    with open("tasks.data", "wb") as f:
        pickle.dump([tasks, completed_tasks], f)

def load_tasks():
    try:
        with open("tasks.data", "rb") as f:
            global tasks, completed_tasks
            tasks, completed_tasks = pickle.load(f)
            update_task_list()
    except FileNotFoundError:
        pass  # No saved data found, continue with empty lists

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Task entry and button
task_entry = tk.Entry(window, width=50)
task_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.grid(row=0, column=3, padx=5, pady=10)

# Task list
task_list_label = tk.Label(window, text="Tasks:")
task_list_label.grid(row=1, column=0, padx=5, pady=5)
task_list = tk.Listbox(window, width=50)
task_list.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Buttons for managing tasks
delete_button = tk.Button(window, text="Delete", command=delete_task)
delete_button.grid(row=3, column=0, padx=5, pady=5)
complete_button = tk.Button(window, text="Mark Complete", command=mark_complete)
complete_button.grid(row=3, column=1, padx=5, pady=5)

# Completed tasks list
completed_list_label = tk.Label(window, text="Completed Tasks:")
completed_list_label.grid(row=4, column=0, padx=5, pady=5)
completed_list = tk.Listbox(window, width=50)
completed_list.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

# Save and load buttons
save_button = tk.Button(window, text="Save Tasks", command=save_tasks)
save_button.grid(row=6, column=0, padx=5, pady=5)
load_button = tk.Button(window, text="Load Tasks", command=load_tasks)
load_button.grid(row=6, column=1, padx=5, pady=5)

# Load tasks on startup
load_tasks()

# Start the main event loop
window.mainloop()
