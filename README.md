# Candy Realm

A command-line board game built in Python where human and AI players race through a candy-themed board by drawing cards and matching them to board spaces.

## Features

- Supports 1–4 human players
- Automatically fills remaining player slots with AI opponents
- Configurable deck size
- Randomized card draws
- Human and AI turn logic
- Interactive board display
- Special spaces with unique effects
- Input validation
- Win detection
- Automatic deck regeneration

## Game Mechanics

Players begin at `START` and draw cards containing board-space identifiers. A player moves to the next matching space ahead of their current position.

Two special spaces affect gameplay:

- **X — Unlucky Rubber Ducky:** the player skips their next turn.
- **S — Quick Slide:** the player immediately moves to the `E` space.

The first player to reach `GOAL` wins.

## Technologies

- Python
- Lists and dictionaries
- Functions
- Loops and conditionals
- Randomization
- Input validation
- State management

## Running the Game

Make sure Python 3 is installed, then run:

```bash
python Candy_Realm.py
```

Follow the prompts to choose the number of human players and configure the deck.

## Project Background

This project began as an introductory programming project and was later cleaned up and organized as a portfolio project. The portfolio version preserves the original game's core mechanics while improving naming, structure, validation, and user-facing messages.
