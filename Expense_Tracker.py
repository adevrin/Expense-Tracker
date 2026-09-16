expenses = []  # Initial empty list

def add_expense():
    temp_dict = {}
    expense_nme = str(input("What is your new expense?\n"))  # Name of expense
    while True:
        try:
        # Price of expense
            expense_price = float(input("How much does it cost\n"))
            break
        except ValueError:
            print("Please input numbers only!")
    # What category the expense fits into
    expense_catag = input("What is the category?\n").lower()
    # Checks if the category was already there
    if expense_catag not in expenses:
        temp_dict[expense_catag] = {"name": expense_nme,
                              "price": expense_price}
        expenses.append(temp_dict)
        print(expenses)
    else:
        expense_catag["name"] = expense_nme
        expense_catag["price"] = expense_price
        print(f"You have added {expense_nme} with the price of {expense_price} to your expenses")


def remove_expense(expense_rmv):
# Asks user for the name of the expense to be removed
        for index in range(len(expenses)): # Iterates through each category in expenses
            for catag in expenses[index]: # Iterates through each key in the category
                if expense_rmv in expenses[index][catag]:
                    removed = expenses[index][catag].pop([expense_rmv])
                    return removed
                else:
                    return f"You do not have any expenses called {expense_rmv}"


def veiw_expenses():
    for catag in expenses:
        mini_list = []
        catag = expenses.keys()
        print(f"CATERGORY ----> {catag.upper()}")
        for value in catag.values():
            mini_list.append(value)
        print(f"{mini_list[0]} {mini_list[1]}")
