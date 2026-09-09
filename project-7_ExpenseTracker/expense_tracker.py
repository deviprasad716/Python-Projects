import json
from pathlib import Path

print("===== EXPENSE TRACKER =====")
print("1. Add Expense.")
print("2. View Expenses.")
print("3. Total Expenses.")
print("4. Filter by Category.")
print("5. Exit.")

def load_expense():
    if Path("expenses.json").exists():
        with open("expenses.json","r") as file:
            return json.load(file)

    else:
        return []

expenses=load_expense()

def add_expense():
    amount=float(input("Enter amount: "))
    category=input("Enter category: ")
    description=input("Enter description: ")
    date=input("Enter date: ")

    return {
        'amount':amount,
        'category':category,
        'description':description,
        'date':date
    }

def save_expenses(expenses):
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)    

while True:

    choice = int(input("Enter choice: "))

    if choice == 1:

        expense=add_expense()
        expenses.append(expense)
        save_expenses(expenses)

        response = input("Add another expense? ")

        while response.lower() == "yes":

            expense=add_expense()

            expenses.append(expense)

            save_expenses(expenses)

            response = input("Add another expense? ")

    elif choice == 2:

        print("===== ALL EXPENSES =====")

        for index, expense in enumerate(expenses, start=1):
            print(f"\nExpense {index}")
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Date: {expense['date']}")

    elif choice == 3:

        total=0

        for expense in expenses:
            total+=expense['amount']

        print(f"Total Expense: ₹{total}")

    elif choice ==4:
        category=input("Enter category: ")

        for expense in expenses:
            if expense['category'].lower()==category.lower():
                print(f"Amount: ₹{expense['amount']}")
                print(f"Category: {expense['category']}")
                print(f"Description: {expense['description']}")
                print(f"Date: {expense['date']}")

    elif choice == 5:
        print("Thank you for using Expense Tracker!")
        break
