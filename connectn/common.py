from enum import Enum
import numpy as np
from typing import Callable, Tuple
from typing import Optional

BoardPiece = np.int8  # The data type of the board
NO_PLAYER = BoardPiece(0)  # board[i, j] == NO_PLAYER where the position is empty
PLAYER1 = BoardPiece(1)  # board[i, j] == PLAYER1 where player 1 has a piece
PLAYER2 = BoardPiece(2)  # board[i, j] == PLAYER2 where player 2 has a piece

PlayerAction = np.int8  # The column to be played


class SavedState:
    pass


class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0


GenMove = Callable[
    [np.ndarray, BoardPiece, Optional[SavedState]],  # Arguments for the generate_move function
    Tuple[PlayerAction, Optional[SavedState]]  # Return type of the generate_move function
]


def initialize_game_state() -> np.ndarray:
    """
    Initialises the board
    :return: an numpy array of dimension 6X7
    """
    return np.zeros((6, 7), dtype=BoardPiece)


def pretty_print_board(input_board: np.ndarray) -> str:
    return '\n'.join([str(row) for row in input_board[::-1]])


def string_to_board(pp_board: str) -> np.ndarray:
    pass


def check_valid_action(d_board, action, player) -> bool:
    return d_board[5, action] == NO_PLAYER


def apply_player_action(d_board, action, player, copy=False) -> tuple:
    # Check if we can place it in that column
    if check_valid_action(d_board, action, player):
        if copy:
            copied_board = np.copy(d_board)
        else:
            copied_board = d_board

        for row in range(6):
            if copied_board[row, action] == NO_PLAYER:
                copied_board[row, action] = player
                break
    else:
        raise Exception('Cannot place player in that particular position')

    return copied_board, d_board


def connected_four(d_board, player, last_action=None) -> bool:
    rows = d_board.shape[0]
    cols = d_board.shape[1]
    if not (last_action in np.arange(rows)):
        for i in range(rows):
            for j in range(cols):
                element = player
                # check row
                if j <= 3 and element == d_board[i, j + 1] and element == d_board[i, j + 2] and element == d_board[
                    i, j + 3]:
                    return True

                # check column
                if i <= 3 and element == d_board[i + 1, j] and element == d_board[i + 2, j] and element == d_board[
                    i + 3, j]:
                    return True

                # right diagonal
                if i <= 2 and j <= 3:
                    if element == d_board[i + 1, j + 1] and element == d_board[i + 2, j + 2] and element == d_board[
                        i + 3, j + 3]:
                        return True

                # left diagonal
                if i <= 2 and j >= 3:
                    if element == d_board[i + 1, j - 1] and element == d_board[i + 2, j - 2] and element == \
                            d_board[i + 3, j - 3]:
                        return True

                return False


def check_end_state(c4_board, player) -> GameState:
    if connected_four(c4_board, player):
        return GameState.IS_WIN
    elif check_board_full(c4_board):
        return GameState.IS_DRAW
    else:
        return GameState.STILL_PLAYING


def check_board_full(c4_board) -> bool:
    for row in range(6):
        for col in range(7):
            if c4_board[row, col] == NO_PLAYER:
                return False

    return True


def get_free_row(d_board, action) -> int:
    for row in range(6):
        if d_board[row, action] == NO_PLAYER:
            return row
    return -1


def get_free_columns(d_board) -> np.ndarray:
    col_list = []
    for col in range(7):
        if d_board[5, col] == NO_PLAYER:
            col_list.append(col)
    return col_list