import numpy as np
from connectn.common import BoardPiece
import connectn.common as cm


def test_pretty_print_board():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    pp_board = cm.pretty_print_board(board)
    test_board = np.zeros((6, 7), dtype=BoardPiece)
    test_board[0, 0] = cm.PLAYER1
    str_test_board = '\n'.join(['\t'.join([str(cell) for cell in row]) for row in test_board[::-1]])
    assert pp_board.__eq__(str_test_board)


def test_string_to_board():
    board = cm.initialize_game_state()
    pp_board = cm.pretty_print_board()
    retrieved_board = cm.string_to_board(pp_board)
    assert isinstance(retrieved_board, np.ndarray)
    assert board.dtype == BoardPiece
    assert board.shape == (6, 7)
    assert np.all(board == 0)


def test_initialize_game_state():
    board = cm.initialize_game_state()

    assert isinstance(board, np.ndarray)
    assert board.dtype == BoardPiece
    assert board.shape == (6, 7)
    assert np.all(board == 0)
