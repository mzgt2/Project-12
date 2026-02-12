# Project-12

## Number Guessing Game 🎯

A simple command-line number guessing game where you try to guess a randomly generated number between 1 and 100.

## Requirements
```bash
pip install art
```

## How to Run
```bash
python number_guessing_game.py
```

## How to Play

1. The game generates a random number between 1 and 100
2. Choose your difficulty:
   - **Easy**: 10 attempts
   - **Hard**: 5 attempts
3. Make guesses and receive hints:
   - "Too low" if your guess is below the number
   - "Too high" if your guess is above the number
4. Win by guessing correctly before running out of attempts
5. Play again or exit after each round

## Game Rules

- You must guess a **whole number** between 1 and 100
- Each incorrect guess costs you one attempt
- The game provides feedback after each guess
- You win by guessing the exact number
- You lose if you run out of attempts

## Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy

Make a guess: 50
Too low.
Guess again.
You have 9 remaining to guess the number.

Make a guess: 75
Too high.
Guess again.
You have 8 remaining to guess the number.

Make a guess: 63
You guessed correct! The random number was 63.
```

## Features

- Two difficulty levels (Easy and Hard)
- Input validation for difficulty selection
- Input validation for numeric guesses only
- Real-time attempt counter
- Replay functionality without restarting
- Clear feedback on each guess
- ASCII art logo display

## What I Learned

Building this project helped me practice:

- **Random number generation** - Using Python's `random` module for game logic
- **Input validation** - Handling both string and numeric input validation with `.isdigit()`
- **Game loop design** - Managing nested loops for rounds and attempts
- **User feedback** - Providing clear, helpful messages throughout gameplay
- **Edge case handling** - Validating user input to prevent crashes
- **Conditional logic** - Implementing comparison logic and difficulty settings
- **Flow control** - Managing game state with flags and counters

This project reinforced clean input handling and creating an engaging user experience in the terminal.

Enjoy! 🎲
