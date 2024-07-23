import tkinter as tk

# Global variables (consider using a data structure like a list for contacts)
contacts = []
current_contact_index = None

def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_text.get("1.0", tk.END)  # Get text from Text widget

    if name and phone_number:  # Validate required fields
        contact = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        update_contact_list()
        clear_entry_fields()

def view_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone_number']}")

def search_contact():
    search_term = search_entry.get()
    if search_term:
        found_contacts = []
        for contact in contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
                found_contacts.append(contact)
        contact_list.delete(0, tk.END)
        for contact in found_contacts:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone_number']}")
    else:
        view_contact_list()  # Display all contacts if search term is empty

def update_contact():
    if current_contact_index is not None:
        contact = contacts[current_contact_index]
        contact["name"] = name_entry.get()
        contact["phone_number"] = phone_entry.get()
        contact["email"] = email_entry.get()
        contact["address"] = address_text.get("1.0", tk.END)
        contacts[current_contact_index] = contact
        update_contact_list()
        clear_entry_fields()
        set_current_contact(None)  # Clear current selection

def delete_contact():
    if current_contact_index is not None:
        contacts.pop(current_contact_index)
        update_contact_list()
        clear_entry_fields()
        set_current_contact(None)  # Clear current selection

def select_contact(event):
    selected_index = contact_list.curselection()[0]
    set_current_contact(selected_index)
    contact = contacts[selected_index]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact["name"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["phone_number"])
    email_entry.delete(0, tk.END)
    email_entry.insert(0, contact["email"])
    address_text.delete("1.0", tk.END)
    address_text.insert(tk.END, contact["address"])

def set_current_contact(index):
    global current_contact_index
    current_contact_index = index

def clear_entry_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Contact Information")
window.configure(bg="#f5f5f5")  # Light gray background

# Labels
name_label = tk.Label(window, text="Name:", font=("Arial", 12), bg="#e0e0e0")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
phone_label = tk.Label(window, text="Phone Number:", font=("Arial", 12), bg="#e0e0e0")
phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
email_label = tk.Label(window, text="Email:", font=("Arial", 12), bg="#e0e0e0")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
address_label = tk.Label(window, text="Address:", font=("Arial", 12), bg="#e0e0e0")
address_label.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

# Entry fields
name_entry = tk.Entry(window, font=("Arial", 12))
name_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
phone_entry = tk.Entry(window, font=("Arial", 12))
phone_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
email_entry = tk.Entry(window, font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
address_text = tk.Text(window, font=("Arial", 12), height=3, width=30)
address_text.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")

# Buttons
add_button = tk.Button(window, text="Add Contact", font=("Arial", 12), bg="#99ff99", command=add_contact)
add_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
view_button = tk.Button(window, text="View All", font=("Arial", 12), bg="#e0e0e0", command=view_contact_list)
view_button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
search_entry = tk.Entry(window, font=("Arial", 12))
search_entry.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
search_button = tk.Button(window, text="Search", font=("Arial", 12), bg="#ffff99", command=search_contact)
search_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
update_button = tk.Button(window, text="Update", font=("Arial", 12), bg="#e0e0e0", command=update_contact)
update_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
delete_button = tk.Button(window, text="Delete", font=("Arial", 12), bg="#ff9999", command=delete_contact)
delete_button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

# Contact list
contact_list = tk.Listbox(window, font=("Arial", 12), selectmode=tk.SINGLE)
contact_list.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
contact_list.bind("<ButtonRelease-1>", select_contact)  # Bind selection event

# Start the main event loop
window.mainloop()

