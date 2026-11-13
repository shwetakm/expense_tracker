def show_main_menu():
    print("============================= Main Menu ===================================")
    print("New: Add New Expense File | View: View Expense File | Exit: Exit the App")
    print(" ")
    user_choice = input("Enter your choice: ")
    return user_choice.strip().lower()

def show_expense_menu():
    print("============================= Sub Menu ===================================")
    print("Add: Enter New Expense Entry | Export: Export file to CSV | Filter: Filter Expenses | Return: Return to Main Menu")
    print(" ")
    user_choice = input("Enter your choice: ")
    return user_choice.strip().lower()



