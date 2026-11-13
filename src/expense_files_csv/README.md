
# CSV Expense Files

This folder contains the CSV files exported from the JSON expense files.

When the user selects the Export option from the expense submenu, the application creates a CSV file using the same filename as the original JSON file.

The CSV file contains the following columns:

- `category`
- `amount`
- `date`
- `description`

These exported files can be opened using Microsoft Excel or other spreadsheet applications.

The CSV export functionality is handled by the `export_expenses_to_csv()` function in `expense_operations/file_operations.py`.
