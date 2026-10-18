def show_main_menu():
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)

def show_expense_menu():
    print("Add: Enter New Expense | Edit: Edit the Expense | Delete: Delete the expense | Save: Save the Expense | Return: Return to Main Menu")
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)

def show_export_menu():
    print("Export: Export the Expense | Exit: Exit the App")
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)

def add_new_expense_file():
    print("Adding a new expense file...")
    # Logic to add a new expense file goes here

def load_existing_expense_file():
    print("Loading an existing expense file...")
    # Logic to load an existing expense file goes here
