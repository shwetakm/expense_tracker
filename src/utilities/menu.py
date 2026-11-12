def show_main_menu():
    print("============================= Main Menu ===================================")
    print("New: Add New File | View: View Expense File | Exit: Exit the App")
    print(" ")
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)

def show_expense_menu():
    print("============================= Sub Menu ===================================")
    print("Add: Enter New Expense | Export: Export to CSV | Filter: Filter Expenses | Return: Return to Main Menu")
    print(" ")
    user_choice = input("Enter your choice: ")
    return str.lower(user_choice)



