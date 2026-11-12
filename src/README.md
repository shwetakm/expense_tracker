
# Expense Tracker

## About the Project

This is a Python-based Expense Tracker application that helps users manage their monthly expenses. Users can create expense files, add new expenses, view existing expenses, filter expenses, and export expense details to CSV files.

The application uses JSON files to store expense records.

## Project Structure

```text
Expense_Tracker/
│
├── README.md
├── main.py
│
├── expense_operations/
│   ├── README.md
│   └── file_operations.py
│
├── utilities/
│   ├── README.md
│   ├── menu.py
│   └── expense.py
│
├── expense_files_json/
│   ├── README.md
│   └── JSON expense files
│
└── expense_files_csv/
    ├── README.md
    └── CSV exported files
```

## Files and Folders

-  main.py:  Starts the application and displays the main menu.
-  expense_operations:  Contains functions to create, view, add, filter, and export expense records.
-  utilities:  Contains the menu functions and Expense class.
-  expense_files_json:  Stores expense records in JSON format.
-  expense_files_csv:  Stores exported expense records in CSV format.

## Features

1. Create a new expense file.
2. View existing expense files.
3. Add new expense entries.
4. Filter expenses by category or date range.
5. Export expenses to CSV.

## Object-Oriented Programming

An Expense class is used to represent individual expense entries. It stores the expense category, amount, date, and description.

The `to_dict()` method converts an Expense object into a dictionary before saving it to the JSON file.

## How to Run

Run the following command from the project root directory:

```bash
python main.py
```
