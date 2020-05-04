import numpy as np
from sympy.utilities import pytest

from connectn.common import BoardPiece
import connectn.common as cm


def test_pretty_print_board():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    pp_board = cm.pretty_print_board(board)
    test_board = np.zeros((6, 7), dtype=BoardPiece)
    test_board[0, 0] = cm.PLAYER1
    str_test_board = '\n'.join([str(row) for row in test_board[::-1]])
    assert pp_board.__eq__(str_test_board)


'''def test_string_to_board():
    board = cm.initialize_game_state()
    pp_board = cm.pretty_print_board(board)
    retrieved_board = cm.string_to_board(pp_board)
    assert isinstance(retrieved_board, np.ndarray)
    assert board.dtype == BoardPiece
    assert board.shape == (6, 7)
    assert np.all(board == 0)'''


def test_initialize_game_state():
    board = cm.initialize_game_state()

    assert isinstance(board, np.ndarray)
    assert board.dtype == BoardPiece
    assert board.shape == (6, 7)
    assert np.all(board == 0)


def test_apply_player_action():
    board = cm.initialize_game_state()

    copied_board, board = cm.apply_player_action(board, 3, cm.PLAYER1)
    test_board = np.zeros((6, 7), dtype=BoardPiece)
    test_board[0, 3] = cm.PLAYER1
    assert np.all(test_board.__eq__(board))


def test_connected_four():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 0] = cm.PLAYER1
    board[2, 0] = cm.PLAYER1
    board[3, 0] = cm.PLAYER1
    assert cm.connected_four(board, cm.PLAYER1)


def test_check_board_full():
    board = cm.initialize_game_state()
    assert ~cm.check_board_full(board)


def test_check_end_state():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 0] = cm.PLAYER1
    board[2, 0] = cm.PLAYER1
    board[3, 0] = cm.PLAYER1
    assert cm.GameState.IS_WIN.__eq__(cm.check_end_state(board, cm.PLAYER1))
