import json

filepath = "expenses_data.json"
# expense_rmv = str(input("Which expense do you want to remove?\n")).lower()
# expense_rmv_catag = str(input("Which category do you want to completely remove?\n")).lower()
# budget = str(input("What do you want to set your monthly budget as?\n")).lower()

expenses = []  # Initial empty list
budget = 0 # Initial 0 budget

def add_expense(expense_nme, expense_price, expenses):
    temp_list = []
    temp_dict = {}

    expense_nme = str(input("What is your new expense?\n")).lower()  # Name of expense

    while True:
        try:
        # Price of expense
            expense_price = float(input("How much does it cost\n"))
            break
        except ValueError:
            print("Please input numbers only!\n")

    # What category the expense fits into
    expense_catag = input("What is the category?\n").lower()

    if len(expenses) < 1:
        temp_list.append({"name": expense_nme,
                          "price": expense_price})
        temp_dict[expense_catag] = temp_list
        expenses.append(temp_dict)
        return f"Added {expense_nme}, price {expense_price} to NEW category {expense_catag}\n"

    # Checks if the category was already there
    for index in range(len(expenses)):
        if expense_catag in expenses[index]:
            temp_list.append({"name": expense_nme,
                            "price": expense_price})
            expenses[index][expense_catag] += temp_list
            return f"Added {expense_nme}, price {expense_price} to category {expense_catag}\n"
        elif index == len(expenses) - 1:
            temp_list.append({"name": expense_nme,
                            "price": expense_price})
            temp_dict[expense_catag] = temp_list
            expenses.append(temp_dict)
            return f"Added {expense_nme}, price {expense_price} to NEW category {expense_catag}\n"


def remove_expense(expense_rmv, expenses):
    # Asks user for the name of the expense to be removed
    for index in range(len(expenses)): # Iterates through each list in expenses
        for catag in expenses[index]: # Iterates through each category in expenses
            for dict in expenses[index][catag]:
                if expense_rmv == dict["name"]:
                    expenses[index][catag].remove(dict)
                    return f"Removed {expense_rmv}\n"

    return f"You do not have any expenses called {expense_rmv}\n"


def remove_category(expense_rmv_catag, expenses):
    for index in range(len(expenses)):
        for catag in expenses[index]:
            if expense_rmv_catag == catag:
                removed_catag = expenses.pop(index)
                return removed_catag

    return f"'{expense_rmv_catag}' could not be found\n"


def view_expenses(expenses):
    if len(expenses) < 1:
        return "You have no expenses\n"
    for index in range(len(expenses)):
        for catag in expenses[index]:
            print(f"CATERGORY ----> {catag.upper()}\n")
            for dict in expenses[index][catag]:
                print(f"{dict['name']}, £{dict['price']}\n")


def monthly_budget(budget, expenses):
    choice = str(input("would you like to set a budget? yes or no\n")).lower().strip()
    if choice == "yes":
        budget = str(input("What do you want to set your monthly budget as?\n")).lower()
    if budget <= 0:
        return "Budget could not be registered"
    total = 0
    for index in range(len(expenses)):
        for catag in expenses[index]:
            for dict in expenses[index][catag]:
                total += dict["price"]
    difference = budget - total
    if difference < 0:
        print(f"Spent over the budget by £{abs(difference)}\n" )
    else:
        print(f"£{difference} budget remaining\n")
    return f"Total price: £{total}, Budget: {budget}"

def save(expenses, budget, filepath):
    all_data = {
        "expenses": expenses,
        "budget": budget
    }
    try:
        with open(filepath, "w") as file:
            json.dump(all_data, file)
            return "Data has been saved\n"
    except FileNotFoundError:
        return []

def load_expenses(expenses, budget, filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
        all_data += data
        expenses += all_data["expenses"]
        budget += all_data["budget"]
        return "Data  has been loaded\n"

while True:
    option = str(input("""=== Expense Tracker ===

1. Add expense
2. Remove expense
3. Remove category
4. View expenses
5. Monthly budget
6. Save
7. Exit

Choose an option:\n""")).lower().strip(" ")
    if option == ("1" or "addexpense"):
        expense_nme = str(input("What is your new expense?\n")).lower()
        add_expense
    elif option == ("2" or "removeexpense"):
        expense_rmv = str(input("Which expense do you want to remove?\n")).lower()
        remove_expense
    elif option == ("3" or "removecategory"):
        expense_rmv_catag = str(input("Which category do you want to completely remove?\n")).lower()
        remove_category
    elif option == ("4" or "viewexpense"):
        view_expenses
    elif option == ("5" or "monthlybudget"):
        monthly_budget
    elif option == ("6" or "save"):
        save
    elif option == ("7" or "exit"):
        break
    else:
        print("Make sure your option is between 1 and 7 inclusive, or type the option")
