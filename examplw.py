
# EXPENSE TRACKER

expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "title": title,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\n--- Your Expenses ---")

            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['title']}")
                print(f"   Amount: Rs. {expense['amount']}")
                print(f"   Category: {expense['category']}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expenses: Rs.", total)

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to delete.")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(i, expense["title"])

            number = int(input("Enter expense number to delete: "))

            if 1 <= number <= len(expenses):
                expenses.pop(number - 1)
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number.")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
