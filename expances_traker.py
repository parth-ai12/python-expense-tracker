expenses = []

while True:
    print("\n💰 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))

    elif choice == "2":
        for item in expenses:
            print(item[0], "-", item[1])

    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        print("Total:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice")