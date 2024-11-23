import tkinter as tk
from tkinter import messagebox
from cleaner import clean_emails  # Import the cleaning logic

# Function to run the email cleaner
def run_cleaner():
    username = email_entry.get()
    password = password_entry.get()
    sender = sender_entry.get()

    if not username or not password or not sender:
        messagebox.showerror("Error", "All fields must be filled out!")
        return

    # Call the cleaning function
    result = clean_emails(username, password, sender)
    messagebox.showinfo("Result", result)

# Create the UI
root = tk.Tk()
root.title("Email Cleaner")

# Email field
tk.Label(root, text="Email Address:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

# Password field
tk.Label(root, text="App Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Sender field
tk.Label(root, text="Sender Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
sender_entry = tk.Entry(root, width=30)
sender_entry.grid(row=2, column=1, padx=10, pady=5)

# Run button
run_button = tk.Button(root, text="Run Cleaner", command=run_cleaner)
run_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()