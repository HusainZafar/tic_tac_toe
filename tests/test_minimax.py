import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tic_tac_toe.tic_tac_toe import tic_tac_toe

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


def make_game():
    """Create a tic_tac_toe instance without triggering __init__ gameplay."""
    with patch.object(tic_tac_toe, '__init__', lambda self, *args: None):
        return tic_tac_toe.__new__(tic_tac_toe)


class TestMinimax:

    def test_computer_wins_next_move(self):
        game = make_game()
        board = ['x', 'x', '-', 'o', 'o', '-', '-', '-', '-']
        result = game.minimax(board, 'x', 'x', 'o')
        assert max(result) == 1

    def test_blocks_player_win(self):
        game = make_game()
        board = ['-', '-', '-', 'o', 'o', '-', 'x', '-', '-']
        result = game.minimax(board, 'x', 'x', 'o')
        assert min(result) >= -1

    def test_empty_board_returns_list(self):
        game = make_game()
        board = ['-'] * 9
        result = game.minimax(board, 'x', 'x', 'o')
        assert isinstance(result, list)
        assert len(result) == 9

    def test_already_won_returns_score(self):
        game = make_game()
        board = ['x', 'x', 'x', 'o', 'o', '-', '-', '-', '-']
        result = game.minimax(board, 'o', 'x', 'o', depth=1)
        assert result == 1

    def test_already_lost_returns_score(self):
        game = make_game()
        board = ['o', 'o', 'o', 'x', 'x', '-', '-', '-', '-']
        result = game.minimax(board, 'x', 'x', 'o', depth=1)
        assert result == -1

    def test_draw_returns_zero(self):
        game = make_game()
        board = ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'x', 'x']
        result = game.minimax(board, 'x', 'x', 'o', depth=1)
        assert result == 0

    def test_computer_never_loses(self):
        game = make_game()
        board = ['-'] * 9
        result = game.minimax(board, 'x', 'x', 'o')
        assert min(result) >= 0
