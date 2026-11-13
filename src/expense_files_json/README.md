
# JSON Expense Files

This folder contains the expense files created by the application.

Each file stores expense records in JSON format. Users can create separate files for different months.

For example:

- january_2026.json
- february_2026.json
- march_2026.json

Each expense record contains the following details:

- `category`
- `amount`
- `date`
- `description`

When a new expense is added, the application saves the details in the selected JSON file.

The expense records are managed using functions from `expense_operations/file_operations.py`.
