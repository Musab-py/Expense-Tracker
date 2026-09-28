import ast

List_of_expenses = []

while True:

    print("----- Expense Tracker -----")
    print("CHOICES:")
    print("1. Add Expense")
    print("2. Calculate Expense")
    print("3. Calculate Total")
    print("4. Category Summary")
    print("5. Search Expense")
    print("6. Delete Expense")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Expense
    if choice == 1:

        Amount = int(input("Enter Amount: "))
        Category = input("Enter Category: ")
        Description = input("Enter Description: ")
        Date = input("Enter Date: ")

        expense = {
            "amount": Amount,
            "category": Category,
            "description": Description,
            "date": Date
        }

        List_of_expenses.append(expense)

        file = open("expenses.txt", "a")
        file.write(str(expense) + "\n")
        file.close()
        print("Your expense has been added!!")


    # 2. Calculate Number of Expenses
    elif choice == 2:

        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        print("The number of expenses are:", len(data))


    # 3. Calculate Total
    elif choice == 3:

        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        total_expense = 0

        for line in data:
            expense = ast.literal_eval(line)
            total_expense += expense["amount"]

        print("Your total expense is:", total_expense)


    # 4. Category Summary
    elif choice == 4:

        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        print("===== EXPENSES =====")

        for line in data:
            expense = ast.literal_eval(line)

            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Date:", expense["date"])
            print("-------------------")


    # 5. Search Expense
    elif choice == 5:

        search = input("Enter the Category you want to search: ")

        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        found = False

        for line in data:
            expense = ast.literal_eval(line)

            if expense["category"] == search:
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print("Date:", expense["date"])
                print("-------------------")

                found = True

        if found == False:
            print("Your desired expense was not found.")


    # 6. Delete Expense
    elif choice == 6:

        search_to_delete = input(
            "Enter the Category of Expense you want to Delete: "
        )

        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        found = False
        new_data = []

        for line in data:
            expense = ast.literal_eval(line)

            if expense["category"] == search_to_delete and found == False:
                found = True
            else:
                new_data.append(line)

        file = open("expenses.txt", "w")
        file.writelines(new_data)
        file.close()

        if found:
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")


    # 7. Exit
    elif choice == 7:

        print("Thank you for using our Expense Tracker")
        break


    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")
