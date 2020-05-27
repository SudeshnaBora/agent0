import numpy as np
from agents.common.common import BoardPiece
from agents.common import common as cm
import pytest


def test_initialize_game_state():
    board = cm.initialize_game_state()

    assert isinstance(board, np.ndarray)
    assert board.dtype == BoardPiece
    assert board.shape == (6, 7)
    assert np.all(board == 0)


def test_pretty_print_board():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    pp_board = cm.pretty_print_board(board)
    test_board = np.zeros((6, 7), dtype=BoardPiece)
    test_board[0, 0] = cm.PLAYER1
    str_test_board = '\n'.join([str(row) for row in test_board[::-1]])
    assert pp_board.__eq__(str_test_board)


# test to check if given player action is valid (positive case)
def test_valid_action_true():
    board = cm.initialize_game_state()
    assert cm.check_valid_action(board, 6)


# checks if the given player action is valid (invalid/negative case)
def test_valid_action_false():
    board = cm.initialize_game_state()
    board[5, 0] = cm.PLAYER1
    assert not cm.check_valid_action(board, 0)


def test_apply_player_action():
    c_board = cm.initialize_game_state()

    copied_board, board = cm.apply_player_action(c_board, 3, cm.PLAYER1)
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


# checks if the board is full (negative case)
def test_check_board_full_false():
    board = cm.initialize_game_state()
    assert ~cm.check_board_full(board)


# checks if board is full (positive case). Leveraging the idea that in \
# case of full board , the topmost row will not be empty
def test_check_board_full_true():
    board = cm.initialize_game_state()
    board[5, 0] = cm.PLAYER1
    board[5, 1] = cm.PLAYER1
    board[5, 2] = cm.PLAYER1
    board[5, 3] = cm.PLAYER1
    board[5, 4] = cm.PLAYER1
    board[5, 5] = cm.PLAYER1
    board[5, 6] = cm.PLAYER1
    assert cm.check_board_full(board)


def test_check_end_state_column():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 0] = cm.PLAYER1
    board[2, 0] = cm.PLAYER1
    board[3, 0] = cm.PLAYER1
    assert cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER1)
    assert not cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER2)


def test_check_end_state_row():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 3] = cm.PLAYER1
    assert cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER1)
    assert not cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER2)


def test_check_end_state_left_diagonal():
    board = cm.initialize_game_state()
    board[0, 1] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[2, 1] = cm.PLAYER1
    board[3, 1] = cm.PLAYER2
    board[0, 2] = cm.PLAYER2
    board[1, 2] = cm.PLAYER2
    board[2, 2] = cm.PLAYER2
    board[0, 3] = cm.PLAYER1
    board[1, 3] = cm.PLAYER2
    board[0, 4] = cm.PLAYER2
    print(cm.pretty_print_board(board))
    assert cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER2)
    assert not cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER1)


def test_get_free_row():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    assert 1 == cm.get_free_row(board, 0)


# checks if any row is free (negative case).
def test_get_free_row_negative():
    board = np.ones((6, 7), dtype=BoardPiece)
    assert -1 == cm.get_free_row(board, 5)


# Testing the IS_DRAW scenario
def test_end_state_draw():
    board = 5 * np.ones((6, 7), dtype=BoardPiece)
    assert cm.GameState.IS_DRAW == cm.check_end_state(board, cm.PLAYER1)


def test_get_free_column():
    board = cm.initialize_game_state()
    board[5, 0] = cm.PLAYER1
    board[5, 1] = cm.PLAYER2
    cols = np.array((2, 3, 4, 5, 6))
    assert np.all(np.equal(cols, cm.get_free_columns(board)))


def test_connected_four_right_diagonal():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[2, 2] = cm.PLAYER1
    board[3, 3] = cm.PLAYER1
    assert cm.connected_four(board, cm.PLAYER1)


def test_apply_player_action_exception():
    board = cm.initialize_game_state()
    board[5, 6] = cm.PLAYER1
    with pytest.raises(Exception, match='Cannot place player in that particular position'):
        cm.apply_player_action(board, 6, cm.PLAYER2)


def test_apply_player_action_copy():
    board = cm.initialize_game_state()
    cp, board = cm.apply_player_action(board, 6, cm.PLAYER1, True)
    assert ~np.all(cp == board)
    assert cp[0, 6] == 1


def test_connected4_column_false():
    board = cm.initialize_game_state()
    board[0, 1] = cm.PLAYER2
    board[1, 1] = cm.PLAYER1
    board[2, 1] = cm.PLAYER1
    board[3, 1] = cm.PLAYER1
    assert ~cm.connected_four(board, cm.PLAYER1)

