import utilities.menu as utilities
import expense_operations.file_operations as file_ops

print("Welcome to the Expense Tracker Application")

print("Available Expense Files:")
file_ops.list_existing_expense_files()

print("================================================================")
print("New: Add New File | View: View Expense File | Exit: Exit the App")
print("================================================================")



app_running_flag = True

while app_running_flag:
    main_menu = utilities.show_main_menu()

    if main_menu == "new":
       file_ops.add_new_expense_file()
    elif main_menu == "view":
         print("Please enter the file name without extension:")
         file_name = input().strip().lower()
         file_name += ".json" 
         file_ops.view_expense_file(file_name)
    elif main_menu == "exit":
        print("Exiting the application.")
        app_running_flag = False    
    else:
        print("Invalid choice. Please try again.")