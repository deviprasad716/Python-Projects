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