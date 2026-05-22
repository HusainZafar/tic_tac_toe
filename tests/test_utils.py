import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tic_tac_toe import utils
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestGetMoveInput:

    @patch('builtins.input', return_value='5')
    def test_valid_digit(self, mock_input):
        assert utils.get_move_input() == 5

    @patch('builtins.input', return_value='1')
    def test_valid_lower_bound(self, mock_input):
        assert utils.get_move_input() == 1

    @patch('builtins.input', return_value='9')
    def test_valid_upper_bound(self, mock_input):
        assert utils.get_move_input() == 9

    @patch('builtins.input', return_value=' 3 ')
    def test_whitespace_around_valid_digit(self, mock_input):
        assert utils.get_move_input() == 3

    @patch('builtins.input', return_value='abc')
    def test_non_numeric_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value='')
    def test_empty_string_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value=' ')
    def test_whitespace_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value='0')
    def test_zero_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value='10')
    def test_out_of_range_high_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value='-1')
    def test_negative_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value='1.5')
    def test_float_returns_none(self, mock_input):
        assert utils.get_move_input() is None

    @patch('builtins.input', return_value='!@#')
    def test_special_characters_returns_none(self, mock_input):
        assert utils.get_move_input() is None


class TestCheckEmpty:

    def test_empty_board(self):
        board = ['-'] * 9
        assert utils.check_empty(board) is True

    def test_one_move_played(self):
        board = ['-'] * 9
        board[0] = 'x'
        assert utils.check_empty(board) is False

    def test_full_board(self):
        board = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
        assert utils.check_empty(board) is False


class TestCheckWin:

    def test_no_win_empty_board(self):
        board = ['-'] * 9
        result = utils.check_win(board, 'x', 'o')
        assert result[0] == 0

    def test_top_row_win(self):
        board = ['x', 'x', 'x', '-', '-', '-', '-', '-', '-']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'x']

    def test_middle_row_win(self):
        board = ['-', '-', '-', 'o', 'o', 'o', '-', '-', '-']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'o']

    def test_bottom_row_win(self):
        board = ['-', '-', '-', '-', '-', '-', 'x', 'x', 'x']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'x']

    def test_left_column_win(self):
        board = ['o', '-', '-', 'o', '-', '-', 'o', '-', '-']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'o']

    def test_middle_column_win(self):
        board = ['-', 'x', '-', '-', 'x', '-', '-', 'x', '-']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'x']

    def test_right_column_win(self):
        board = ['-', '-', 'o', '-', '-', 'o', '-', '-', 'o']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'o']

    def test_diagonal_top_left_win(self):
        board = ['x', '-', '-', '-', 'x', '-', '-', '-', 'x']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'x']

    def test_diagonal_top_right_win(self):
        board = ['-', '-', 'o', '-', 'o', '-', 'o', '-', '-']
        result = utils.check_win(board, 'x', 'o')
        assert result == [1, 'o']

    def test_draw(self):
        board = ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'x', 'x']
        result = utils.check_win(board, 'x', 'o')
        assert result[0] == 2

    def test_game_in_progress(self):
        board = ['x', 'o', '-', '-', 'x', '-', '-', '-', '-']
        result = utils.check_win(board, 'x', 'o')
        assert result[0] == 0


class TestTheMove:

    def test_picks_best_move(self):
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        lst = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        result = utils.the_move(board, lst)
        assert result == 1

    def test_picks_from_multiple_best(self):
        board = ['-', 'x', '-', '-', '-', '-', '-', '-', '-']
        lst = [1, 1, 0, 0, 0, 0, 0, 0]
        result = utils.the_move(board, lst)
        assert board[result] == '-'
