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
    if expense_catag not in temp_dict:
        temp_dict[expense_catag] = {"name": expense_nme,
                              "price": expense_price}
        expenses.append(temp_dict)
        print(expenses)
    else:
        expense_catag["name"] = expense_nme
        expense_catag["price"] = expense_price
        print(f"You have added {expense_nme} with the price of {expense_price} to your expenses")

def remove_expense():
    expense_rmv = input("")

add_expense()
