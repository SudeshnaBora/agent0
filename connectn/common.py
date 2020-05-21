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
    """
    Stringifies the board

    :parameter input_board: the connect 4 playing board
    :return: a stringified version of the board
    """
    return '\n'.join([str(row) for row in input_board[::-1]])


def string_to_board(pp_board: str) -> np.ndarray:
    pass


def check_valid_action(d_board: np.ndarray, action: np.int8) -> bool:
    """
    Checks validity of the action applied on the board

    :parameter d_board: the playing board of type np.ndarray
    :parameter action : the column number where the next piece is to be placed.
    :return: a boolean flag stating True if valid otherwise False
    """
    return d_board[5, action] == NO_PLAYER


def apply_player_action(d_board: np.ndarray, action: np.int8, player: BoardPiece, copy=False) -> tuple:
    """
    Applies player action on the board

    :parameter d_board: the playing board of type np.ndarray
    :parameter action: the column number where the next piece is to be placed.
    :parameter player: the player making the move
    :parameter copy: Optional parameter stating if we want to make a copy of the board. This is used during the minimax algorithm to predict the future moves

    :return: a boolean flag stating True if valid otherwise False
    """
    # Check if we can place it in that column
    if check_valid_action(d_board, action):
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


def connected_four(d_board: np.ndarray, player: BoardPiece, last_action=None) -> bool:
    """
    Check if connect 4 or a win sequence has formed in the board

    :parameter d_board: the playing board of type np.ndarray
    :parameter player: the player making the move
    :parameter last_action: the last action on the board (optional parameter)

    :return: a boolean flag stating True if connect 4 takes place otherwise False
    """
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


def check_end_state(c4_board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Applies player action on the board

    :parameter c4_board: the playing board of type np.ndarray
    :parameter player: the player making the move

    :return: Whether there is a win , a draw or the match is still going on.
    """
    if connected_four(c4_board, player):
        return GameState.IS_WIN
    elif check_board_full(c4_board):
        return GameState.IS_DRAW
    else:
        return GameState.STILL_PLAYING


def check_board_full(c4_board: np.ndarray) -> bool:
    """
    Check if the board is full

    :parameter c4_board: the playing board of type np.ndarray

    :return: a boolean flag stating True if full otherwise False
    """
    for row in range(6):
        for col in range(7):
            if c4_board[row, col] == NO_PLAYER:
                return False

    return True


def get_free_row(d_board: np.ndarray, action: np.int8) -> int:
    """
    Get the row that has free space

    :parameter d_board: the playing board of type np.ndarray
    :parameter action: the column number where the next piece is to be placed.

    :return: the row which has free space
    """
    for row in range(6):
        if d_board[row, action] == NO_PLAYER:
            return row
    return -1


def get_free_columns(d_board: np.ndarray) -> list:
    """
    Retrieve a list of free columns

    :parameter d_board: the playing board of type np.ndarray

    :return: returns a list of column index numbers.
    """
    col_list = []
    for col in range(7):
        if d_board[5, col] == NO_PLAYER:
            col_list.append(col)
    return col_list