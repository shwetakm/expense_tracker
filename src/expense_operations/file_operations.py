import os

from utilities.menu import show_expense_menu

EXPENSE_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "expense_files")
)

def list_existing_expense_files():
        folder = EXPENSE_FOLDER

        for x in os.listdir(folder):
            if x.endswith(".json"):
                print(x)

def add_new_expense_file():
    print("Please enter the file name (Recommended format is monthname_year, e.g., January_2024):")
    file_name = input().strip().lower()
    if not file_name.endswith(".json"): 
        file_name += ".json"   
        file_path = os.path.join(EXPENSE_FOLDER, file_name)
                 

        try:
             with open(file_path, 'x') as f:
                 print(file_path+" created successfully.")
                 view_expense_file(file_name)       
        except FileExistsError:
            print("The expense file already exists. Please choose a different name.")
    else:
        print("error while creating the file. Please try again.")


def view_expense_file(file_name):
    print("Viewing the expense file:", file_name)
    file_path = os.path.join(EXPENSE_FOLDER, file_name)

    try:
        with open(file_path, 'r') as f:
            print(f"Viewing contents of {file_name}:")
            print(f.read())
            show_expense_menu()
    except FileNotFoundError:
        print("The specified expense file was not found.")
    ()


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

