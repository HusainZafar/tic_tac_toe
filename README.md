# TicTacToe-AI

A command-line Tic Tac Toe game with an unbeatable AI opponent and local multiplayer. The AI uses the Minimax algorithm to evaluate every possible game state and play optimally. Includes an option to display win/loss/draw predictions for every playable box, per move.

## How to Play

The board uses a numpad-style layout for selecting positions:

```
 7 | 8 | 9
---|---|---
 4 | 5 | 6
---|---|---
 1 | 2 | 3
```

Enter a number (1-9) to place your move in the corresponding position.

When win chance display is enabled, each empty cell shows:
- **W** — this move leads to a win
- **D** — this move leads to a draw
- **L** — this move leads to a loss

## How the AI Works

The AI uses the [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax) to explore all possible future game states from the current board. It assumes both players play optimally:
- On the computer's turn, it picks the move with the highest score (maximizing).
- On the player's turn, it assumes the player picks the best move for themselves (minimizing).

This makes the AI unbeatable — the best outcome a player can achieve is a draw.

## Install

### From pip:
```
pip install tic_tac_toe
```

### Locally for development:
```
git clone https://github.com/HusainZafar/tic_tac_toe.git
cd tic_tac_toe
pip install -e .
```

This installs the package in editable mode — any changes you make to the source code will take effect immediately without reinstalling.

## Usage

Single player mode (default):
```
tic_tac_toe --mode s
```

Two player mode:
```
tic_tac_toe --mode t
```

Help:
```
tic_tac_toe --help
```

## Development

### Run tests:
```
pip install pytest
pytest tests/ -v
```

### Run linter:
```
pip install ruff
ruff check .
```

## Project Structure

```
tic_tac_toe/
  tic_tac_toe.py   # Main game logic, minimax AI, single/two player modes
  utils.py         # Board display, win detection, input validation, move selection
  constants.py     # Board state and keyboard-to-index mapping
tests/
  test_utils.py    # Tests for utility functions and input validation
  test_minimax.py  # Tests for AI correctness
```

## Demo

[![Demo Video](http://img.youtube.com/vi/jl7qYpLRXPM/0.jpg)](https://www.youtube.com/watch?v=jl7qYpLRXPM)

## Screenshots

![Single Player](screenshots/single.png)

![Output](screenshots/output.png)

![Result](screenshots/result.png)

## License

MIT
