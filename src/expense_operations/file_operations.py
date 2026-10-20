import os

def list_existing_expense_files():
        folder = os.path.join(os.path.dirname(__file__), "..", "expense_files")

        for x in os.listdir(folder):
            if x.endswith(".json"):
                print(x)


def add_new_expense_file():
    print("Adding a new expense file...")
    # Logic to add a new expense file goes here

def load_existing_expense_file():
    print("Loading an existing expense file...")
    # Logic to load an existing expense file goes here