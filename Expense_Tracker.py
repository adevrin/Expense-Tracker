from Expense_functions import add_expense # expenses
from Expense_functions import remove_expense # expense_rmv, expenses
from Expense_functions import remove_category # expense_rmv_catag, expenses 
from Expense_functions import view_expenses # expenses
from Expense_functions import monthly_budget # expenses, budget
from Expense_functions import save # expenses, budget, filepath
from Expense_functions import load_expenses # expenses, budget, filepath

filepath = "expenses_data.json"

expenses = []  # Initial empty list
budget = 0  # Initial 0 budget

load_expenses(expenses, budget, filepath)

while True:
    option = str(input("""=== Expense Tracker ===

    1. Add expense
    2. Remove expense
    3. Remove category
    4. View expenses
    5. Monthly budget
    6. Save
    7. Exit
    Choose an option:\n""")).lower().replace(" ", "")

    if option == "1" or option == "addexpense":
        add_expense(expenses)

    elif option == "2" or option == "removeexpense":
        expense_rmv = str(
            input("Which expense do you want to remove?\n")).lower()
        remove_expense(expense_rmv, expenses)

    elif option == "3" or option == "removecategory":
        expense_rmv_catag = str(
            input("Which category do you want to completely remove?\n")).lower()
        remove_category(expense_rmv_catag, expenses)

    elif option == "4" or option == "viewexpense":
        view_expenses(expenses)

    elif option == "5" or option == "monthlybudget":
        budget = monthly_budget(expenses, budget)
    
    elif option == "6" or option == "save":
        save(expenses, budget, filepath)

    elif option == "7" or option == "exit": 
        break

    else:
        print("Make sure your option is between 1 and 7 inclusive, or type the option")
