
# Expense Operations

This folder contains the functions used to manage expense files.

## file_operations.py

This file handles the main expense-related operations in the application.

The functions in this file are used to:

- Display the available expense files.
- Create a new expense file.
- Open and view an existing expense file.
- Add new expense entries.
- Filter expenses by category or date range.
- Export expense records to CSV.

This file also imports the Expense class from `utilities/expense.py` to create expense objects when a user adds a new expense.

Before saving an expense to the JSON file, the Expense object is converted into a dictionary using the `to_dict()` method.

The JSON files are stored in the `expense_files_json` folder, and exported CSV files are saved in the `expense_files_csv` folder.
