def add_expense(date, description, category, amount, notes):
    import customtkinter as ctk
# File path for storing expenses data
DATA_FILE = "expenses_data.json"

def add_expense(description, category, amount, date, notes):
    # Load existing expense data from the file
    expenses_data = load_expenses_data()

    # Create a new expense dictionary
    new_expense = {
        'description': description,
        'category': category,
        'amount': amount,
        'date': date,
        'notes': notes
    }

    # Add the new expense to the data
    expenses_data.append(new_expense)

    # Save the updated expense data to the file
    save_expenses_data(expenses_data)

def load_expenses_data():
    try:
        with open(DATA_FILE, 'r') as file:
            expenses_data = json.load(file)
    except FileNotFoundError:
        expenses_data = []
    return expenses_data

def save_expenses_data(expenses_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses_data, file)

def get_expenses():
    # Load expense data from the file
    expenses_data = load_expenses_data()

    # Return the list of expenses
    return expenses_data
    pass

def get_expenses():
   import json
    try:
        with open(DATA_FILE, 'r') as file:
            expenses_data = json.load(file)
    except FileNotFoundError:
        expenses_data = []
    return expenses_data
    pass