import datetime

def record_expense(amount, category, description):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {amount} USD - {category} - {description}\n"

    with open("expenses.txt", "a") as file:
        file.write(entry)

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                print(expense)
    except FileNotFoundError:
        print("No expenses recorded yet.")

while True:
    print("\nExpense Tracker Menu:")
    print("1. Record Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        amount = float(input("Enter the expense amount : "))
        category = input("Enter the expense category: ")
        description = input("Enter a brief description: ")
        record_expense(amount, category, description)
        print("Expense recorded successfully.")
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")