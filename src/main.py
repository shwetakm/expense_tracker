import utilities.menu as utilities

print("Welcome to the Expense Tracker Application")
print("New: Add New File | Load: Open existing File | Exit: Exit the App")

app_running_flag = True

while app_running_flag:
    main_menu = utilities.show_main_menu()

    if main_menu == "new":
       utilities.add_new_expense_file()
    elif main_menu == "load":
         utilities.load_existing_expense_file()
    elif main_menu == "exit":
        print("Exiting the application.")
        app_running_flag = False    
    else:
        print("Invalid choice. Please try again.")