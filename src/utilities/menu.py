def show_main_menu():
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)

def show_expense_menu():
    print("Add: Enter New Expense | Export: Export to CSV | Filter: Filter Expenses | Return: Return to Main Menu")
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)

def show_export_menu():
    print("Export: Export the Expense | Exit: Exit the App")
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)


