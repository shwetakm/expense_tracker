# File operations for the Expense Tracker

import csv
import json
import os

from utilities.menu import show_expense_menu
from utilities.expense import Expense

EXPENSE_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "expense_files_json")
)

CSV_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "expense_files_csv")
)

#show already available expense files
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
                 json.dump([], f)
                 
             print(file_path+" created successfully.")
             view_expense_file(file_name)       
        except FileExistsError:
            print("Error: The expense file already exists. Please choose a different name.")


#view function for new file and load existing file and show submenu 
def view_expense_file(file_name):

    try:
        print("Viewing the expense file:", file_name)
        file_path = os.path.join(EXPENSE_FOLDER, file_name)
        with open(file_path, 'r') as f:
            expenses = json.load(f)
            for item in expenses:
                print(f"{item['date']} | {item['category']} | ${item['amount']} | {item['description']}")

            submenu_running_flag = True
            
            while submenu_running_flag:
                user_choice = show_expense_menu() # new entry | export | filter

                if user_choice == "add":
                    add_new_expense_entry(file_path)
                    print("New expense entry added successfully.")
                elif user_choice == "export":
                    export_expenses_to_csv(file_path)
                elif user_choice == "filter":
                    filter_expenses(file_path)
                elif user_choice == "return":
                    submenu_running_flag = False
                    print("Returning to the main menu...")
                else:
                    print("Error: Invalid choice. Please try again.")

    except FileNotFoundError:
        print("Error: The specified expense file was not found.")


#add new expense entry to the file
def add_new_expense_entry(file_path):
    print("Expense categories are: Food, Education, Utilities, Health")
    expense_category = input("Enter the expense category: ")
    expense_amount = float(input("Enter the expense amount: "))
    expense_date = input("Enter the expense date (YYYY-MM-DD): ")
    expense_description = input("Enter the expense description: ")

    # Create an Expense object 
    new_expense_entry = Expense(
    expense_category,
    expense_amount,
    expense_date,
    expense_description
    )

    try: # get existing json entry, apend new entry
        with open(file_path, 'r') as f:
            existing_json_string = json.load(f)
        
        existing_json_string.append(new_expense_entry.to_dict())

    except Exception as e:
        print("Error occurred while reading existring json entries")

    try: #write back to the file
        with open(file_path, 'w') as f:
            json.dump(existing_json_string, f, indent=4)
    except Exception as e:
        print("Error occurred while writing new entry to the file")


#filter expenses from the file
def filter_expenses(file_path):
    try:
        with open(file_path, 'r') as f:
            expenses = json.load(f)
        print("------------Filter and Display Expenses------------")
        print("1. Food |  2. Education |  3. Utilities |  4. Health |  5. Date Range |  6. Return")
        category_filter = input("Enter your choice ")
        categories = {
                        "1": "Food",
                        "2": "Education",
                        "3": "Utilities",
                        "4": "Health"
                    }
        
        if category_filter in categories:
                print("Category | Date | Amount | Description")
                for item in expenses:
                    if item["category"] == categories[category_filter]:
                        print(f'{item["category"]} | {item["date"]} | ${item["amount"]} | {item["description"]}')

        elif category_filter == "5":
                start_date = input("Start date (YYYY-MM-DD): ")
                end_date = input("End date (YYYY-MM-DD): ")

                for item in expenses:
                    if start_date <= item["date"] <= end_date:
                        print(f'{item["date"]} | ${item["amount"]} | {item["description"]}')

        elif category_filter == "6":
                return

        else:
                print("Invalid choice.")

    except Exception as e:
            print("Error occurred while filtering expenses")


def export_expenses_to_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            expenses = json.load(f)

        file_name = os.path.basename(file_path).replace(".json", ".csv")
        csv_file_path = os.path.join(CSV_FOLDER, file_name)

        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ["category", "amount", "date", "description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)

        print(f"Expenses exported successfully to {csv_file_path}")

    except Exception as e:
        print("Error occurred while exporting expenses to CSV")