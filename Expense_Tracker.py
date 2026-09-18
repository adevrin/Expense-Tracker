# expense_nme = str(input("What is your new expense?\n"))
# expense_rmv = str(input("Which expense do you want to remove?\n"))

expenses = []  # Initial empty list

def add_expense(expense_nme, expense_price, expenses):
    temp_list = []
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
    for index in range(len(expenses)): # Iterates through each category in expenses
        for catag in expenses[index]: # Iterates through each key in the category
            if expense_rmv in expenses[index][catag]:
                removed = expenses[index][catag].pop([expense_rmv])
                return removed
            else:
                return f"You do not have any expenses called {expense_rmv}"


def remove_category():


def view_expenses(expenses):
    for catag in expenses:
        mini_list = []
        catag = expenses.keys()
        print(f"CATERGORY ----> {catag.upper()}")
        for value in catag.values():
            mini_list.append(value)
        print(f"{mini_list[0]}, £{mini_list[1]}")
