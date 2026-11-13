# Main application for the Expense Tracker
# first show all available expense files and provide menu options to add new expense file | view existing expense file | exit

import utilities.menu as utilities
import expense_operations.file_operations as file_ops

class ExpenseTrackerApp:
    def __init__(self):
        self.manager = file_ops.ExpenseOpsManager()
        
    def run(self):

        print("============================= Welcome to the Expense Tracker Application =============================\n")

        print("Available Expense Files:")
        self.manager.list_existing_expense_files()
        print(" ")

        app_running_flag = True

        while app_running_flag:
            main_menu = utilities.show_main_menu()

            if main_menu == "new":
                self.manager.add_new_expense_file()
            elif main_menu == "view":
                self.manager.view_expense_file()
            elif main_menu == "exit":
                print("Exiting the application.")
                app_running_flag = False    
            else:
                print("Error: Invalid choice. Please try again.")


if __name__ == "__main__":
    ExpenseTrackerApp().run()