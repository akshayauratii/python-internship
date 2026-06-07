
print("Expense Tracker Started")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = input("Amount: ")
        print("Expense Added!")

    elif choice == "2":
        print("No expenses yet.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")