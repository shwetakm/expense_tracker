import json
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

#create a new file and redirect to view_expense_file function
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


#view function for new file and load existing file and show submenu 
def view_expense_file(file_name):
    print("Viewing the expense file:", file_name)
    file_path = os.path.join(EXPENSE_FOLDER, file_name)

    try:
        with open(file_path, 'r') as f:
            print(f.read())
            user_choice = show_expense_menu() # new entry | export | filter

            if user_choice == "add":
                new_expense = add_new_expense_entry(file_path)
                print("New expense entry added:", new_expense)
            elif user_choice == "export":
                print("Exporting the expense file to CSV...")
            elif user_choice == "filter":
                print("Filtering expenses...")
            elif user_choice == "return":
                print("Returning to the main menu...")
            else:
                print("Invalid choice. Returning to the main menu.")  

    except FileNotFoundError:
        print("The specified expense file was not found.")
    ()


def add_new_expense_entry(file_path):
    print("Expense categories are: Food, Education, Utilities, Health")
    expense_category = input("Enter the expense category: ")
    expense_amount = float(input("Enter the expense amount: "))
    expense_date = input("Enter the expense date (YYYY-MM-DD): ")
    expense_description = input("Enter the expense description: ")
    new_expense_entry = {
        "category": expense_category,   
        "amount": expense_amount,
        "date": expense_date,
        "description": expense_description
    }
    try: # get existing json entry, apend new entry
        with open(file_path, 'r') as f:
            existing_json_string = json.load(f)
        
        existing_json_string.append(new_expense_entry)
    except Exception as e:
        print("Error occurred while reading existring json entries")

    try: #write back to the file
        with open(file_path, 'w') as f:
            json.dump(existing_json_string, f, indent=4)
    except Exception as e:
        print("Error occurred while writing new entry to the file")