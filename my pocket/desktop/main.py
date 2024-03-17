from expenses import add_expense
from gui import create_gui

def main():
    import tkinter as tk
import expenses  # Assuming you have an expenses.py module with relevant functions

def submit_expense():
    # Retrieve the entered data from the form
    description = description_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()
    notes = notes_entry.get()

    # Call the add_expense() function from expenses.py and pass the entered data
    expenses.add_expense(description, category, amount, date, notes)

    # Clear the form fields
    description_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)

def display_expenses():
    # Retrieve the list of expenses from expenses.py
    expense_list = expenses.get_expenses()

    # Clear any previous data in the expenses listbox
    expenses_listbox.delete(0, tk.END)

    # Display the expenses in the listbox
    for expense in expense_list:
        expenses_listbox.insert(tk.END, expense)

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Expenses Tracker")

    # Create the expense form
    expense_frame = tk.Frame(window)
    expense_frame.pack(padx=10, pady=10)

    # Description input
    description_label = tk.Label(expense_frame, text="Description:")
    description_label.grid(row=0, column=0, sticky="w")
    description_entry = tk.Entry(expense_frame)
    description_entry.grid(row=0, column=1, padx=5, pady=5)

    # Category input
    category_label = tk.Label(expense_frame, text="Category:")
    category_label.grid(row=0, column=2, sticky="w")
    category_entry = tk.Entry(expense_frame)
    category_entry.grid(row=0, column=3, padx=5, pady=5)

    # Amount input
    amount_label = tk.Label(expense_frame, text="Amount:")
    amount_label.grid(row=1, column=0, sticky="w")
    amount_entry = tk.Entry(expense_frame)
    amount_entry.grid(row=1, column=1, padx=5, pady=5)

    # Date input
    date_label = tk.Label(expense_frame, text="Date:")
    date_label.grid(row=1, column=2, sticky="w")
    date_entry = tk.Entry(expense_frame)
    date_entry.grid(row=1, column=3, padx=5, pady=5)

    # Notes input
    notes_label = tk.Label(expense_frame, text="Notes:")
    notes_label.grid(row=2, column=0, sticky="w")
    notes_entry = tk.Entry(expense_frame)
    notes_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

    # Submit button
    submit_button = tk.Button(window, text="Submit", command=submit_expense)
    submit_button.pack(pady=10)

    # Expenses listbox
    expenses_listbox = tk.Listbox(window)
    expenses_listbox.pack(padx=10, pady=10)

    # Display button
    display_button = tk.Button(window, text="Display Expenses", command=display_expenses)
    display_button.pack(pady=10)

    # Start the GUI event loop
    window.mainloop()

# Call the create_gui() function to display the GUI form
    create_gui()

if __name__ == "__main__":
    main()