expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expense: ₹{total}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank you! 👋")
        break
    else:
        print("Invalid choice!\n")
