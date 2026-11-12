
# Utilities

This folder contains the menu functions and Expense class used in the application.

## menu.py

This file contains two functions:

- `show_main_menu()` – Displays the main menu where the user can add a new expense file, view an existing file, or exit the application.
- `show_expense_menu()` – Displays the submenu where the user can add expenses, export expenses to CSV, filter expenses, or return to the main menu.

## expense.py

This file contains the Expense class, which is used to create expense objects.

The class has the following attributes:

- `category` – Stores the expense category.
- `amount` – Stores the expense amount.
- `date` – Stores the expense date.
- `description` – Stores the expense description.

It also has a `to_dict()` method that converts the expense object into a dictionary. This is needed because the application stores expense details in JSON format.

The Expense class helps keep the expense details together instead of creating a dictionary directly every time a new expense is added.
