# expense_nme = str(input("What is your new expense?\n")).lower()
# expense_rmv = str(input("Which expense do you want to remove?\n")).lower()
# expense_rmv_catag = str(input("Which category do you want to completely remove?\n")).lower()
# budget = str(input("What do you want to set your monthly budget as?\n")).lower()

expenses = []  # Initial empty list

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
            print("Please input numbers only!")

    # What category the expense fits into
    expense_catag = input("What is the category?\n").lower()

    if len(expenses) < 1:
        temp_list.append({"name": expense_nme,
                          "price": expense_price})
        temp_dict[expense_catag] = temp_list
        expenses.append(temp_dict)
        return f"Added {expense_nme}, price {expense_price} to NEW category {expense_catag}"

    # Checks if the category was already there
    for index in range(len(expenses)):
        if expense_catag in expenses[index]:
            temp_list.append({"name": expense_nme,
                            "price": expense_price})
            expenses[index][expense_catag] += temp_list
            return f"Added {expense_nme}, price {expense_price} to category {expense_catag}"
        elif index == len(expenses) - 1:
            temp_list.append({"name": expense_nme,
                            "price": expense_price})
            temp_dict[expense_catag] = temp_list
            expenses.append(temp_dict)
            return f"Added {expense_nme}, price {expense_price} to NEW category {expense_catag}"


def remove_expense(expense_rmv, expenses):
    # Asks user for the name of the expense to be removed
    for index in range(len(expenses)): # Iterates through each list in expenses
        for catag in expenses[index]: # Iterates through each category in expenses
            for dict in expenses[index][catag]:
                if expense_rmv == dict["name"]:
                    expenses[index][catag].remove(dict)
                    return f"Removed {expense_rmv}"

    return f"You do not have any expenses called {expense_rmv}"


def remove_category(expense_rmv_catag, expenses):
    for index in range(len(expenses)):
        for catag in expenses[index]:
            if expense_rmv_catag == catag:
                removed_catag = expenses.pop(index)
                return removed_catag

    return f"'{expense_rmv_catag}' could not be found"


def view_expenses(expenses):
    if len(expenses) < 1:
        return "You have no expenses"
    for index in range(len(expenses)):
        for catag in expenses[index]:
            print(f"CATERGORY ----> {catag.upper()}")
            for dict in expenses[index][catag]:
                print(f"{dict['name']}, £{dict['price']}")


def monthly_budget(budget, expenses):
    total = 0
    for index in range(len(expenses)):
        for catag in expenses[index]:
            for dict in expenses[index][catag]:
                total += dict["price"]

    
