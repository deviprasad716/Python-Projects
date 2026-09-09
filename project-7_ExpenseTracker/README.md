## Project-7 : Expense Tracker

A simple **Expense Tracker** built using Python.

This project allows users to add, view, calculate, and filter expenses.  
All expenses are stored in a JSON file so that the data remains available even after closing the program.

### Features

-  Add Expense
-  View All Expenses
-  Calculate Total Expenses
-  Filter Expenses by Category
-  Save Expenses to JSON
-  Load Expenses from JSON when the program starts
-  Exit the application

### Topics Used

- JSON
- `pathlib`
- File Handling
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements

###  Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

###  How It Works

When the program starts, it checks whether `expenses.json` exists.

* If the file exists → previously saved expenses are loaded.
* If the file doesn't exist → an empty expense list is created.

When a new expense is added, it is saved to `expenses.json`.

Each expense contains:

* Amount
* Category
* Description
* Date

Example:

```python
{
    "amount": 250,
    "category": "Food",
    "description": "Lunch",
    "date": "06-09-2026"
}
```

###  Example Output

```text
===== EXPENSE TRACKER =====
1. Add Expense.
2. View Expenses.
3. Total Expenses.
4. Filter by Category.
5. Exit.

Enter choice: 1
Enter amount: 450
Enter category: Food
Enter description: Dinner
Enter date: 09-09-2026

Add another expense? no

Enter choice: 2

===== ALL EXPENSES =====

Expense 1
Amount: ₹250
Category: Food
Description: Lunch
Date: 06-09-2026

Expense 2
Amount: ₹450
Category: Food
Description: Dinner
Date: 09-09-2026

Enter choice: 3
Total Expense: ₹700

Enter choice: 4
Enter category: Food

Amount: ₹250
Category: Food
Description: Lunch
Date: 06-09-2026

Amount: ₹450
Category: Food
Description: Dinner
Date: 09-09-2026

Enter choice: 5
Thank you for using Expense Tracker!
```

