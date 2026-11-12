# Expense Tracker

A command-line application for managing monthly expense records.

## Project structure

```text
expense_tracker/
├── main.py
├── expense_operations/
│   └── file_operations.py
├── utilities/
│   └── menu.py
├── expense_files_json/
│   └── (monthly expense data files, stored as JSON)
└── expense_files_csv/
    └── (CSV files exported from JSON expense records)
```

## How the application works

1. `main.py` starts the application and displays the main menu.
2. `utilities/menu.py` displays the main menu and the expense-file submenu.
3. `expense_operations/file_operations.py` handles expense-file creation, viewing, adding entries, filtering, and CSV export.
4. `expense_files_json/` stores expense records in JSON format.
5. `expense_files_csv/` stores CSV files exported from the JSON records.

## Run the application

From the project root directory, run:

```bash
python main.py
```

## Main menu options

- **New** — Create a new monthly expense file.
- **View** — Open an existing expense file.
- **Exit** — Close the application.

## Expense-file submenu options

- **Add** — Add a new expense entry.
- **Export** — Export the current expense file to CSV.
- **Filter** — Display expenses by category or date range.
- **Return** — Return to the main menu.

## Expense record fields

Each expense record contains:

- `category`
- `amount`
- `date`
- `description`

The application currently uses JSON files as its main data store and creates CSV files when the user selects the export option.
