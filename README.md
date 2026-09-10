# Python-Projects

## Project-1 : Weight Converter

A simple Python program that converts weight between kilograms and pounds. The program takes the user's weight and preferred unit as input and uses conditional statements to perform the conversion.

### Features

- Takes weight as input from the user.
- Allows the user to choose between kilograms and pounds.
- Converts pounds to kilograms.
- Converts kilograms to pounds.
- Uses conditional statements.
- Displays the converted weight.
- Simple command-line interface.

### Conversion Rules

The program uses the following conversion formulas:

- Pounds → Kilograms: weight × 0.45.
- Kilograms → Pounds: weight ÷ 0.45.

For example:

- 100 lbs → 45 kg
- 45 kg → 100 lbs

### Example Output

```text
Enter your weight: 100
(L)bs or (K)g: l
You are 45.0 kgs..


Enter your weight: 45
(L)bs or (K)g: k
You are 100.0 pounds..
```

## Project-2 : Leap Year Checker

A simple Python program that checks whether a given year is a leap year or not. The program uses conditional statements to apply the standard leap year rules.

### Features

- Takes a year as input from the user
- Checks whether the year is divisible by 4
- Handles century years using the 100 and 400 divisibility rules
- Displays whether the entered year is a leap year or not
- Simple command-line interface

### Leap Year Rules

A year is a leap year if:

- It is divisible by 4
- If it is divisible by 100, it must also be divisible by 400

For example:

- 2024 → Leap year
- 1900 → Not a leap year
- 2000 → Leap year
- 2023 → Not a leap year

### Example Output

```text
Enter the year: 2024

2024 is a leap year..

```

## Project-3 : Number Guessing Game

A simple Python command-line game where the computer randomly selects a number between 1 and 100, and the player has to guess the number within a limited number of attempts. The game provides hints after each guess and has two difficulty modes: Easy and Hard.

### Features

- Generates a random number between 1 and 100.
- Allows the player to choose between Easy and Hard modes.
- Gives hints if the guessed number is too high or too low.
- Validates the difficulty mode input.
- Displays the number of attempts remaining.
- Announces whether the player won or lost.

### Game Rules

The computer randomly selects a number between 1 and 100.

The player can choose between two difficulty levels:

Easy: 10 attempts.
Hard: 5 attempts.

After every guess, the game provides a hint:

Too HIGH: The guessed number is greater than the computer's number.
Too LOW: The guessed number is smaller than the computer's number.
Correct: The player guessed the number and wins the game.

If the player uses all the available attempts without guessing the correct number, the player loses the game.

### Example Output

```text
Welcome to Number Guessing Game!!
Select mode (easy) or (hard): easy
Guess a number we have in the range of 100.

You have 10 number of attempts to guess the number!!
Guess the number? : 50
Too LOW, Guess again..

You have 9 number of attempts to guess the number!!
Guess the number? : 75
Too HIGH, Guess again..

You have 8 number of attempts to guess the number!!
Guess the number? : 63
You guessed the correct number and WON.
```

### Topics learnt

- Random ModuleB
- Conditional Statements
- While Loops
- User Input

## Project-4 : Simple Calculator

A beginner-friendly command-line calculator built with Python. This project allows users to perform basic arithmetic operations through an interactive menu.

### Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Decimal number support
- Invalid choice handling
- Division by zero protection
- Modulus by zero protection
- Continuous operation until the user chooses to exit

### How to Run

Make sure Python is installed on your system.

Run the program using:

```bash
python calculator.py
```

### Example

```text
Enter your choice: 1
Enter first number: 25
Enter second number: 15
Result: 40.0
```

If division or modulus by zero is attempted, the program will continue asking for a valid second number.

### Future Improvements

- Add calculation history
- Add more mathematical operations
- Improve input validation for non-numeric input
- Add a graphical user interface (GUI)

## Project-5 : Student Grade Management System

A beginner-friendly Python OOP project that manages student information, marks, averages, and topper details through a simple menu-driven command-line interface.

This project was built to strengthen my understanding of Object-Oriented Programming (OOP) and apply concepts such as classes, objects, instance methods, lists of objects, input validation, and basic search logic.

### Features

- Add a student
- Display all students
- Search for a student using roll number
- Find the student with the highest average
- Prevent duplicate roll numbers
- Handle invalid menu input
- Calculate student averages
- Handle students with no marks safely
- Exit the program through the menu

### Future Improvements

This project is intentionally kept simple to focus on core Python and OOP concepts.

Possible improvements for a future version:

Update student details
Delete a student
Assign grades automatically
Sort students by average
Save student data to a file
Load student data when the program starts
Add a graphical interface
Store data using a database

### Example Output

```text
===== STUDENT GRADE MANAGEMENT SYSTEM =====

1. Add Student.
2. Display Students.
3. Search Student.
4. Find Topper.
5. Exit

Select the choice:

Example Student Entry

Student Name: Dev
Roll No: 101
Marks: 85 90 92

Student added Successfully....

Example Search

Enter the Roll No: 101

Student Found!
Name : Dev
Roll No : 101
Marks : [85, 90, 92]
Average : 89.0
```

## Project-6 : Contact Book

A beginner-friendly Python project that manages contact information through a simple menu-driven command-line interface.

This project was built to strengthen my understanding of Python dictionaries, nested dictionaries, functions, loops, conditionals, input validation, searching, updating, and deleting data.

### Features

- Add a contact
- Display all contacts
- Search for a contact using name
- Update contact phone number and email
- Delete a contact
- Prevent duplicate contact names
- Handle invalid menu input
- Store contact information using nested dictionaries
- Exit the program through the menu

### Future Improvements

This project is intentionally kept simple to focus on core Python concepts and data handling.

Possible improvements for a future version:

- Update contact name
- Search contacts by phone number or email
- Validate phone numbers
- Validate email addresses
- Sort contacts alphabetically
- Save contact data to a file
- Load contact data when the program starts
- Add a graphical interface
- Store contact data using a database

### Example Output

```text
===== CONTACT ME =====

1. Add Contact.
2. View Contacts.
3. Search Contact.
4. Update Contact.
5. Delete Contact.
6. Exit.

Enter your choice: 1

Enter name: Dev
Enter phone: 9988776655
Enter email: xyz@gmail.com

Contact added successfully.

Example Search

Enter name to search: Dev

Contact found!!
Name: Dev
Phone: 9988776655
Email: xyz@gmail.com
```

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

## Project-8 : Rock Paper Scissors Game

A simple command-line Rock Paper Scissors game built using Python. The player competes against the computer, which randomly chooses Rock, Paper, or Scissors.

### Features

- Interactive gameplay through the terminal
- Random computer choices using Python's `random` module
- ASCII art representation of Rock, Paper, and Scissors
- Win, lose, and draw detection
- Input validation for invalid choices

### Example Output

```text
Enter your choice(Type 0 for Rock, 1 for Paper, 2 for Scisor):0

You chose: Rock
Computer chose: Scissors

You win!
```

## Project-9 : Password Generator

A simple Python program that generates a random password based on the number of letters, numbers, and symbols specified by the user.

### Features

- Generates random passwords
- Includes uppercase and lowercase letters
- Includes digits (0-9)
- Includes special symbols
- User can customize the number of:
  - Letters
  - Numbers
  - Symbols

### Example Output

```text
Welcome to Password Generator!
How many letters you want in your password: 5
How many numbers you want in your password: 3
How many symbols you want in your password: 2

Password: AbXde731!$
```

## Project-10 : Hangman Game

Hangman is a classic word guessing game developed using Python. In this game, the player has to guess the hidden fruit name one letter at a time. For every incorrect guess, a part of the hangman figure is drawn. The game ends when the player either guesses the complete word or loses all available lives.

### Features

- Random fruit word selection for every game.
- User-friendly letter-by-letter guessing system.
- Visual hangman stages displayed after wrong guesses.
- Tracks remaining lives.
- Win and lose conditions implemented.
- Beginner-friendly project structure using separate modules.

### Example Output

In this example, the randomly selected word is **apple**. Each wrong guess changes the appearance of the hangman.

```text
apple
['_', '_', '_', '_', '_']

Guess the letter: z
['_', '_', '_', '_', '_']

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess the letter: x
['_', '_', '_', '_', '_']

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

Guess the letter: a
['a', '_', '_', '_', '_']

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

Guess the letter: p
['a', 'p', 'p', '_', '_']

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

Guess the letter: l
['a', 'p', 'p', 'l', '_']

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

Guess the letter: e
['a', 'p', 'p', 'l', 'e']

You Win!!

```
