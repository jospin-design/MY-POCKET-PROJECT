import customtkinter as ctk
from expenses import add_expense

def create_gui():
    # Create the main window
    window = ctk.CustomTk()
    window.title("Expenses Tracker")

    # Create the expense form
    expense_frame = ctk.CustomFrame(window)
    expense_frame.pack(padx=10, pady=10)

    # Description input
    description_label = ctk.CustomLabel(expense_frame, text="Description:")
    description_label.grid(row=0, column=0, sticky="w")
    description_entry = ctk.CustomEntry(expense_frame)
    description_entry.grid(row=0, column=1, padx=5, pady=5)

    # Category input
    category_label = ctk.CustomLabel(expense_frame, text="Category:")
    category_label.grid(row=0, column=2, sticky="w")
    category_entry = ctk.CustomEntry(expense_frame)
    category_entry.grid(row=0, column=3, padx=5, pady=5)

    # Amount input
    amount_label = ctk.CustomLabel(expense_frame, text="Amount:")
    amount_label.grid(row=1, column=0, sticky="w")
    amount_entry = ctk.CustomEntry(expense_frame)
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    # Date input
    date_label = ctk.CustomLabel(expense_frame, text="Date:")
    date_label.grid(row=1, column=2, sticky="w")
    date_entry = ctk.CustomEntry(expense_frame)
    date_entry.grid(row=1, column=3, padx=5, pady=5)

    # Notes input
    notes_label = ctk.CustomLabel(expense_frame, text="Notes:")
    notes_label.grid(row=2, column=0, sticky="w")
    notes_entry = ctk.CustomEntry(expense_frame)
    notes_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

    def submit_expense():
        # Retrieve the entered data from the form
        description = description_entry.get()
        category = category_entry.get()
        amount = amount_entry.get()
        date = date_entry.get()
        notes = notes_entry.get()

        # Call the add_expense() function from expenses.py and pass the entered data
        add_expense(description, category, amount, date, notes)

        # Clear the form fields
        description_entry.delete(0, ctk.END)
        category_entry.delete(0, ctk.END)
        amount_entry.delete(0, ctk.END)
        date_entry.delete(0, ctk.END)
        notes_entry.delete(0, ctk.END)

    # Submit button
    submit_button = ctk.CustomButton(window, text="Submit", command=submit_expense)
    submit_button.pack(pady=10)

    # Start the GUI event loop
    window.run()

# Call the create_gui() function to display the GUI form
create_gui()