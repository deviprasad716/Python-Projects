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

- Random Module
- Conditional Statements
- While Loops
- User Input



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
