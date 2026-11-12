# expense_operations

This folder contains the functions that perform the main expense-file operations.

## `file_operations.py`

The module is responsible for:

- Listing existing JSON expense files.
- Creating a new expense file.
- Opening and displaying an expense file.
- Adding expense entries to a JSON file.
- Filtering expenses by category or date range.
- Exporting expense records to CSV.

## Dependencies

The module uses Python's built-in `csv`, `json`, and `os` modules. It also imports `show_expense_menu` from `utilities/menu.py`.

## Data folders

The module reads and writes JSON expense files in `expense_files_json/` and writes exported CSV files to `expense_files_csv/`.
