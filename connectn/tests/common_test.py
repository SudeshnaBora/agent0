import numpy as np
from connectn.common import BoardPiece
import connectn.common as cm


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


'''def test_string_to_board():
    board = cm.initialize_game_state()
    pp_board = cm.pretty_print_board(board)
    retrieved_board = cm.string_to_board(pp_board)
    assert isinstance(retrieved_board, np.ndarray)
    assert board.dtype == BoardPiece
    assert board.shape == (6, 7)
    assert np.all(board == 0)'''


def test_valid_action_true():
    board = cm.initialize_game_state()
    assert cm.check_valid_action(board, 6)


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


def test_check_board_full():
    board = cm.initialize_game_state()
    assert ~cm.check_board_full(board)


def test_check_end_state_vertical():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 0] = cm.PLAYER1
    board[2, 0] = cm.PLAYER1
    board[3, 0] = cm.PLAYER1
    assert cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER1)
    assert not cm.GameState.IS_WIN == cm.check_end_state(board, cm.PLAYER2)


def test_check_end_state_horizontal():
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


def test_get_free_column():
    board = cm.initialize_game_state()
    board[5, 0] = cm.PLAYER1
    board[5, 1] = cm.PLAYER2
    cols = np.array((2, 3, 4, 5, 6))
    assert np.all(np.equal(cols, cm.get_free_columns(board)))
