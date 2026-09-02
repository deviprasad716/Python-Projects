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