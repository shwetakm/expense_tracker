import os

from utilities.menu import show_expense_menu

def list_existing_expense_files():
        folder = os.path.join(os.path.dirname(__file__), "..", "expense_files")

        for x in os.listdir(folder):
            if x.endswith(".json"):
                print(x)

def add_new_expense_file():
    print("Please enter the file name (Recommended format is monthname_year, e.g., January_2024):")
    file_name = input().strip().lower()
    if not file_name.endswith(".json"): 
        file_name += ".json"                    

        try:
             with open(file_name, 'x') as f:
                 print(file_name+" created successfully.")
                 view_expense_file()       
        except FileExistsError:
            print("The expense file already exists. Please choose a different name.")
    else:
        print("error while creating the file. Please try again.")


def view_expense_file():
    show_expense_menu()


def add_new_expense_entry():
    print("Expense categories are: Food, Education, Utilities, Health")
    expense_category = input("Enter the expense category: ")
    expense_amount = float(input("Enter the expense amount: "))
    expense_date = input("Enter the expense date (YYYY-MM-DD): ")
    expense_description = input("Enter the expense description: ")
    return {
        "category": expense_category,   
        "amount": expense_amount,
        "date": expense_date,
        "description": expense_description
    }

