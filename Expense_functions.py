import json

filepath = "expenses_data.json"


def add_expense(expenses):
    temp_list = []
    temp_dict = {}
    # Name of expense
    expense_nme = str(input("What is your new expense?\n")).lower()

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
    # Iterates through each list in expenses
    for index in range(len(expenses)):
        # Iterates through each category in expenses
        for catag in expenses[index]:
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
    if len(expenses) <= 0:
        print("You have no expenses\n")
        return
    else:
        for index in range(len(expenses)):
            for catag in expenses[index]:
                print(f"CATERGORY ----> {catag.upper()}\n")
                for dict in expenses[index][catag]:
                    print(f"{dict['name']}, £{dict['price']}\n")
        return


def monthly_budget(expenses, budget):
    print(f"your budget is currently £{budget}")
    budget_add = 0
    while True:
        try:
            choice = str(
                input("would you like to set a budget? yes or no\n")).lower().strip()
            if choice == "yes":
                budget_add = float(
                    input("What do you want to set your monthly budget as?\n"))
                if budget_add <= 0:
                    print(f"Budget could not be registered") 
        except ValueError:
            print("Please enter a number")
        budget = budget_add
        try:
            choice = str(
                input("would you like to see your budget? yes or no\n")).lower().strip()
            if choice == "yes":
                total = 0
                for index in range(len(expenses)):
                    for catag in expenses[index]:
                        for dict in expenses[index][catag]:
                            total += dict["price"]
                difference = budget - total
                if difference < 0:
                    print(f"Spent over the budget by £{abs(difference)}\n")
                else:
                    print(f"£{difference} budget remaining\n")
                    print(f"Total price: £{total}, Budget: {budget}")
                    break
        except ValueError:
            print("Please enter a number")
    budget = budget_add
    return budget

def save(expenses, budget, filepath):
    all_data = {
        "expenses": expenses,
        "budget": budget
    }
    try:
        with open(filepath, "w") as file:
            json.dump(all_data, file)
            print("Data has been saved\n")
            return
    except FileNotFoundError:
        return 


def load_expenses(expenses, budget, filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            all_data = data
            expenses += all_data["expenses"]
            budget += all_data["budget"]
            print("Data has been loaded\n")
            return budget
    except FileNotFoundError:
        return